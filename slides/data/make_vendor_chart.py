#!/usr/bin/env python3
"""Build a vendor coverage chart from university_ai_vendors.csv."""

import csv
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

CSV_PATH = "university_ai_vendors.csv"
OUT_PATH = "../figures/vendor_coverage.pdf"

COLORS = {
    'R1': '#1B4D5C',       # SlateTeal
    'R2': '#3498DB',       # AccentBlue
    'LAC': '#D4A84B',      # UVMGold
    'International': '#8899A6',  # CoolGray
    'System': '#154734',   # UVMGreen
    'Other': '#C0534D',    # SoftCoral
}

with open(CSV_PATH) as f:
    rows = list(csv.DictReader(f))

vendors = ['microsoft', 'openai', 'google', 'anthropic']
vendor_labels = ['Microsoft\nCopilot', 'OpenAI\nChatGPT', 'Google\nGemini', 'Anthropic\nClaude']

# Count by institution type and vendor
types_order = ['R1', 'R2', 'LAC', 'International']
type_totals = Counter(r['type'] for r in rows if r['type'] in types_order)

data = {}
for t in types_order:
    data[t] = []
    t_rows = [r for r in rows if r['type'] == t]
    for v in vendors:
        count = sum(1 for r in t_rows if r[v].strip())
        data[t].append(count)

# --- Figure 1: Grouped bar — share with each vendor, by institution type ---
fig, ax = plt.subplots(figsize=(10, 5.5))

# Compute shares (%) for each vendor × type
us_types = ['R1', 'R2', 'LAC']
us_type_labels = ['R1 Universities\n(n={})'.format(type_totals['R1']),
                  'R2 Universities\n(n={})'.format(type_totals['R2']),
                  'Liberal Arts\nColleges (n={})'.format(type_totals['LAC'])]

shares = {}
for v in vendors:
    shares[v] = []
    for t in us_types:
        t_rows = [r for r in rows if r['type'] == t]
        count = sum(1 for r in t_rows if r[v].strip())
        pct = count / len(t_rows) * 100 if t_rows else 0
        shares[v].append(pct)

x = np.arange(len(vendors))
n_types = len(us_types)
width = 0.22
offsets = [-(width + 0.02), 0, (width + 0.02)]

type_colors = [COLORS['R1'], COLORS['R2'], COLORS['LAC']]

for i, (t, label, color) in enumerate(zip(us_types, us_type_labels, type_colors)):
    vals = [shares[v][i] for v in vendors]
    bars = ax.bar(x + offsets[i], vals, width, label=label,
                  color=color, edgecolor='white', linewidth=0.5)
    # Add percentage labels on bars
    for bar, val in zip(bars, vals):
        if val > 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                    f'{val:.0f}%', ha='center', va='bottom', fontsize=8,
                    fontweight='bold', color=color)

ax.set_xticks(x)
ax.set_xticklabels(vendor_labels, fontsize=12)
ax.set_ylabel('Share of institutions with agreement (%)', fontsize=11)
ax.set_title('Who Has Institutional AI Agreements?',
             fontsize=14, fontweight='bold', color='#1B4D5C')
ax.set_ylim(0, 100)
ax.axhline(y=50, color='#EDF2F0', linewidth=0.8, zorder=0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(loc='upper right', framealpha=0.9, fontsize=9)

total_inst = sum(type_totals[t] for t in us_types)
fig.text(0.5, -0.02,
         f'Based on publicly verifiable agreements at {total_inst} US institutions (June 2026).\n'
         f'Google and Microsoft counts likely undercounted — bundled with existing Workspace/M365 licenses.',
         ha='center', fontsize=8, color='#8899A6', style='italic')

plt.tight_layout()
plt.savefig(OUT_PATH, bbox_inches='tight', dpi=300)
print(f"Saved to {OUT_PATH}")

# --- Figure 2: Heatmap of how many vendors per institution type ---
fig2, ax2 = plt.subplots(figsize=(8, 3.5))

for t in types_order:
    t_rows = [r for r in rows if r['type'] == t]
    vendor_counts = []
    for r in t_rows:
        n = sum(1 for v in vendors if r[v].strip())
        # Also check 'other' column for multi-model platforms
        if r.get('other', '').strip():
            # If 'other' has content but no individual vendor columns, count as 1
            if n == 0:
                n = 1
        vendor_counts.append(n)
    counts = Counter(vendor_counts)
    total = len(t_rows)
    for nv in range(5):
        pct = counts.get(nv, 0) / total * 100 if total else 0
        ax2.barh(t, counts.get(nv, 0), left=sum(counts.get(j, 0) for j in range(nv)),
                color=plt.cm.YlOrRd(nv / 5), edgecolor='white', linewidth=0.5)

ax2.set_xlabel('Number of institutions', fontsize=11)
ax2.set_title('Number of AI Vendors per Institution', fontsize=13, fontweight='bold', color='#1B4D5C')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

legend_patches = [mpatches.Patch(color=plt.cm.YlOrRd(i/5), label=f'{i} vendors') for i in range(5)]
ax2.legend(handles=legend_patches, loc='lower right', fontsize=8, framealpha=0.9)

plt.tight_layout()
fig2.savefig(OUT_PATH.replace('.pdf', '_depth.pdf'), bbox_inches='tight', dpi=300)
print(f"Saved depth chart")

# Print summary stats
print(f"\n=== Summary ===")
print(f"Total institutions: {len(rows)} ({total_inst} in chart)")
for t in types_order:
    print(f"  {t}: {type_totals[t]}")
print()
for v, label in zip(vendors, ['Microsoft', 'OpenAI', 'Google', 'Anthropic']):
    count = sum(1 for r in rows if r[v].strip() and r['type'] in types_order)
    print(f"  {label}: {count}/{total_inst} ({count/total_inst*100:.0f}%)")
