import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

if not os.path.exists("img"):
    os.makedirs("img")

plt.rcParams["font.family"] = "Times New Roman"

# Sample data
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Value': [30, 70, 45, 55, 20, 80]
}
df = pd.DataFrame(data)

# Step 1: Calculate percentage within each Category
df['Percentage'] = df.groupby('Category')['Value'].transform(lambda x: x / x.sum() * 100)

# Step 2: Pivot the table for easy plotting
df_pivot = df.pivot(index='Category', columns='Subcategory', values='Percentage').fillna(0)

# Step 3: Plot 100% stacked bar chart
fig, ax = plt.subplots(figsize=(8, 6))

# Define colors
colors = sns.color_palette("pastel")

# Initialize bottom at 0 for stacking
bottom = pd.Series([0] * len(df_pivot), index=df_pivot.index)

for i, col in enumerate(df_pivot.columns):
    ax.bar(df_pivot.index, df_pivot[col], bottom=bottom, label=col, color=colors[i])
    
    # Add percentage labels inside bars
    for idx in df_pivot.index:
        val = df_pivot.loc[idx, col]
        if val > 0:
            ax.text(idx, bottom[idx] + val/2, f'{val:.1f}%', 
                    ha='center', va='center', fontsize=10, color='black', fontweight='bold')
    
    # Update bottom for next stack
    bottom += df_pivot[col]

# Customize chart
ax.set_title('100% Stacked Bar Chart', fontsize=14, fontweight='bold')
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.set_xlabel('Category', fontsize=12)
ax.set_ylim(0, 100)
ax.legend(title='Subcategory', bbox_to_anchor=(1.05, 1), loc='upper left')
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig("img/stacked_barplots_100.svg", format="svg")
# plt.show()
