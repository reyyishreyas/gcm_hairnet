#!/usr/bin/env python3
"""
Generate publication-quality side-by-side comparison figures.
Layout: models in a grid (left to right, worst → best)
        Ground Truth centered on the right side spanning all rows
"""

import json
import sys
from pathlib import Path
import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.gridspec import GridSpec

# Publication-ready style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica', 'Liberation Sans'],
    'font.size': 11,
    'axes.titlesize': 12,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.spines.left': False,
    'axes.spines.bottom': False,
    'xtick.major.size': 0,
    'ytick.major.size': 0,
    'axes.linewidth': 0.5,
    'axes.edgecolor': '#cccccc',
})

# Custom hazard colormap: safe green → caution yellow → danger red
HAZARD_COLORS = LinearSegmentedColormap.from_list(
    "hazard_risk",
    [
        "#1a9850",
        "#91cf60",
        "#d9ef8b",
        "#fee08b",
        "#fc8d59",
        "#d73027",
        "#b2182b",
    ],
    N=256
)


def load_city_predictions(model_name, city_name, split="test"):
    """Load predictions and targets for a specific city."""
    base = Path("/Users/reyyishreyas/Desktop/gcmh/outputs/experiments") / model_name / split
    
    preds = np.load(base / f"{split}_predictions.npy")
    targets = np.load(base / f"{split}_targets.npy")
    
    cities_path = base / f"{split}_cities.json"
    if cities_path.exists():
        with open(cities_path) as f:
            cities = json.load(f)
    else:
        cities = [f"City {i+1}" for i in range(len(preds))]
    
    try:
        city_idx = cities.index(city_name)
    except ValueError:
        print(f"City '{city_name}' not found in {model_name}. Available: {cities}")
        return None, None, None
    
    return preds[city_idx], targets[city_idx], city_name


def create_side_by_side_figure(models_data, title, output_path, city_name,
                                cmap=HAZARD_COLORS):
    """
    Create a side-by-side comparison figure.
    
    Layout: models in a grid (left to right, worst → best)
            Ground Truth centered on the right side spanning all rows
    """
    n_models = len(models_data)
    
    # Determine grid dimensions: aim for 3 columns, calculate rows
    n_cols_models = 3
    n_rows = math.ceil(n_models / n_cols_models)
    n_cols = n_cols_models + 1  # +1 for GT column
    
    # Figure dimensions
    fig_width = 16
    fig_height = 3.5 * n_rows
    
    fig = plt.figure(figsize=(fig_width, fig_height))
    
    # Use GridSpec for custom layout
    gs = GridSpec(n_rows, n_cols, figure=fig,
                  width_ratios=[1, 1, 1, 0.85],
                  height_ratios=[1] * n_rows,
                  hspace=0.4, wspace=0.2)
    
    targets = models_data[0]['targets']
    vmin, vmax = 0, 1
    
    # Plot models in columns 0-2
    for idx, model_info in enumerate(models_data):
        row = idx // n_cols_models
        col = idx % n_cols_models
        
        ax = fig.add_subplot(gs[row, col])
        preds = model_info['preds']
        r2 = model_info.get('r2', 0)
        mse = model_info.get('mse', 0)
        name = model_info['name']
        
        pred_img = preds.squeeze()
        im = ax.imshow(pred_img, cmap=cmap, vmin=vmin, vmax=vmax, aspect='equal')
        
        # Metrics overlay with clean styling
        metric_text = f"R² = {r2:.3f}\nMSE = {mse:.4f}"
        ax.text(
            0.02, 0.98, metric_text,
            transform=ax.transAxes,
            fontsize=9,
            verticalalignment='top',
            horizontalalignment='left',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='white', alpha=0.92,
                     edgecolor='#dddddd', linewidth=0.5),
            color='#222222',
            family='monospace'
        )
        
        ax.set_title(name, fontsize=10, fontweight='bold', color='#333333', pad=8)
        ax.axis('off')
    
    # Plot Ground Truth in column 3, spanning all rows
    ax_gt = fig.add_subplot(gs[:, n_cols_models])
    gt_img = targets.squeeze()
    im_gt = ax_gt.imshow(gt_img, cmap=cmap, vmin=vmin, vmax=vmax, aspect='equal')
    ax_gt.set_title(f"Ground Truth\n{city_name}", fontsize=11, fontweight='bold',
                    color='#222222', pad=10)
    ax_gt.axis('off')
    
    # Add a subtle border around GT
    for spine in ax_gt.spines.values():
        spine.set_visible(True)
        spine.set_edgecolor('#333333')
        spine.set_linewidth(1.5)
    
    # Add colorbar on the far right
    cbar_ax = fig.add_axes([0.95, 0.15, 0.008, 0.7])
    cbar = fig.colorbar(im_gt, cax=cbar_ax)
    cbar.set_label("Hazard Risk Probability", fontsize=10, rotation=90, labelpad=12)
    cbar.ax.tick_params(labelsize=9)
    cbar.set_ticks([0, 0.25, 0.5, 0.75, 1.0])
    cbar.set_ticklabels(['0.0', '0.25', '0.50', '0.75', '1.0'])
    
    # Main title
    fig.suptitle(title, fontsize=14, fontweight='bold', y=0.98, color='#222222')
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', pad_inches=0.25)
    plt.close(fig)
    print(f"Saved: {output_path}")


def main():
    output_dir = Path("/Users/reyyishreyas/Desktop/gcmh/outputs/experiments/results")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    city_name = "Jammu"
    
    baseline_metrics = {
        'gcm':        {'r2': 0.809871793, 'mse': 0.013963833},
        'vit':        {'r2': 0.702091634, 'mse': 0.021879669},
        'swin':       {'r2': 0.614501834, 'mse': 0.028312642},
        'graphsage':  {'r2': 0.526168000, 'mse': 0.034800000},
        'mha':        {'r2': 0.621401000, 'mse': 0.027806000},
        'nonlocal':   {'r2': 0.709930000, 'mse': 0.021304000},
    }
    
    fusion_metrics = {
        'addition':               {'r2': 0.9538082, 'mse': 0.0033925227},
        'bilinear':               {'r2': 0.94440895, 'mse': 0.0040828465},
        'concat':                 {'r2': 0.80251503, 'mse': 0.014504145},
        'gated':                  {'r2': 0.68688214, 'mse': 0.022996724},
        'cross_attention':        {'r2': 0.64848423, 'mse': 0.025816828},
        'multihead_cross_attention': {'r2': 0.62923914, 'mse': 0.027230268},
        'gis_only':               {'r2': 0.70133114, 'mse': 0.021935526},
        'image_only':             {'r2': 0.62713635, 'mse': 0.02738471},
    }
    
    # Load baseline data (sorted worst → best)
    baseline_order = ['graphsage', 'swin', 'mha', 'vit', 'nonlocal', 'gcm']
    baseline_data = []
    for name in baseline_order:
        preds, targets, _ = load_city_predictions(name, city_name, "test")
        if preds is None:
            continue
        m = baseline_metrics[name]
        baseline_data.append({
            'name': name.replace('_', '-').title(),
            'preds': preds,
            'targets': targets,
            'r2': m['r2'],
            'mse': m['mse'],
        })
    
    # Load fusion data (sorted worst → best)
    fusion_order = ['image_only', 'multihead_cross_attention', 'cross_attention',
                    'gated', 'gis_only', 'concat', 'bilinear', 'addition']
    fusion_data = []
    for name in fusion_order:
        preds, targets, _ = load_city_predictions(name, city_name, "test")
        if preds is None:
            continue
        m = fusion_metrics[name]
        fusion_data.append({
            'name': name.replace('_', '-').title(),
            'preds': preds,
            'targets': targets,
            'r2': m['r2'],
            'mse': m['mse'],
        })
    
    # Create figures
    create_side_by_side_figure(
        baseline_data,
        f"Baseline Models — {city_name} (Test Set, Sorted by R²)",
        output_dir / "baseline_city_comparison.png",
        city_name=city_name
    )
    
    create_side_by_side_figure(
        fusion_data,
        f"Fusion Techniques — {city_name} (Test Set, Sorted by R²)",
        output_dir / "fusion_city_comparison.png",
        city_name=city_name
    )
    
    print(f"\nDone! Generated side-by-side figures for {city_name}.")


if __name__ == "__main__":
    main()
