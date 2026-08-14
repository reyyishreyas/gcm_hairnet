import sys
import torch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader
from models import GCMHAIRNet
from losses import build_loss
from utils.misc import get_device


def main():
    print("Starting training...")
    config_manager = ConfigManager()
    config = config_manager.load("train")
    device = get_device()
    print(f"Using device: {device}")

    print("Loading data...")
    try:
        dataset = GCMHAIRNetDataset(root_dir="./data/processed", split="train")
        loader = build_dataloader(dataset, batch_size=4, shuffle=True, drop_last=True)
        val_dataset = GCMHAIRNetDataset(root_dir="./data/processed", split="val")
        val_loader = build_dataloader(val_dataset, batch_size=4, shuffle=False, drop_last=False)
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    print(f"Train: {len(dataset)} samples, Val: {len(val_dataset)} samples")

    if len(val_dataset) == 0:
        print("Warning: Validation dataset is empty. Skipping validation.")
        val_loader = None

    print("Creating model...")
    model = GCMHAIRNet(config.get("model", {})).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
    loss_fn = build_loss({"type": "mse"})

    print(f"Parameters: {sum(p.numel() for p in model.parameters()):,}")
    print("=" * 60)

    for epoch in range(100):
        model.train()
        train_loss = 0.0
        count = 0

        for batch in loader:
            img = batch["image"].to(device)
            gis = batch["gis"].to(device)
            label = batch["label"].to(device)

            optimizer.zero_grad()
            pred = model(img, gis)
            loss = loss_fn(pred, label)
            loss.backward()
            optimizer.step()

            train_loss += loss.item()
            count += 1

        train_loss /= max(count, 1)

        val_loss = 0.0
        if val_loader is not None:
            model.eval()
            vcount = 0

            with torch.no_grad():
                for batch in val_loader:
                    img = batch["image"].to(device)
                    gis = batch["gis"].to(device)
                    label = batch["label"].to(device)
                    pred = model(img, gis)
                    loss = loss_fn(pred, label)
                    val_loss += loss.item()
                    vcount += 1

            val_loss /= max(vcount, 1)
        else:
            val_loss = train_loss

        print(f"Epoch {epoch+1:3d}/100: train_loss={train_loss:.4f}, val_loss={val_loss:.4f}")

        if (epoch + 1) % 10 == 0:
            checkpoint_dir = Path("checkpoints/gcm_simple")
            checkpoint_dir.mkdir(parents=True, exist_ok=True)
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'train_loss': train_loss,
                'val_loss': val_loss,
            }, checkpoint_dir / f"epoch_{epoch+1:04d}.pt")
            print(f"  Saved checkpoint at epoch {epoch+1}")


if __name__ == "__main__":
    main()
