import torch

class Engine:
    def __init__(self, model, optimizer, scheduler, loss_fn, device, gradient_clip_val=None, gradient_accumulation_steps=1):
        self.model = model
        self.optimizer = optimizer
        self.scheduler = scheduler
        self.loss_fn = loss_fn
        self.device = device
        self.gradient_clip_val = gradient_clip_val
        self.gradient_accumulation_steps = gradient_accumulation_steps
        self.step = 0
    
    def train_step(self, batch):
        self.model.train()
        image = batch["image"].to(self.device)
        gis = batch["gis"].to(self.device)
        label = batch["label"].to(self.device)
        
        preds = self.model(image, gis)
        loss = self.loss_fn(preds, label)
        loss = loss / self.gradient_accumulation_steps
        loss.backward()
        
        if (self.step + 1) % self.gradient_accumulation_steps == 0:
            if self.gradient_clip_val:
                torch.nn.utils.clip_grad_norm_(self.model.parameters(), self.gradient_clip_val)
            self.optimizer.step()
            self.optimizer.zero_grad()
            if self.scheduler and not isinstance(self.scheduler, torch.optim.lr_scheduler.ReduceLROnPlateau):
                self.scheduler.step()
        
        self.step += 1
        return {"loss": loss.item() * self.gradient_accumulation_steps}
    
    def validation_step(self, batch):
        self.model.eval()
        with torch.no_grad():
            image = batch["image"].to(self.device)
            gis = batch["gis"].to(self.device)
            label = batch["label"].to(self.device)
            
            preds = self.model(image, gis)
            loss = self.loss_fn(preds, label)
            
            return {
                "val_loss": loss.item(),
                "preds": torch.sigmoid(preds).cpu(),
                "targets": label.cpu()
            }
