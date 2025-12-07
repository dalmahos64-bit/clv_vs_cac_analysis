# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# 1. Seaborn styling
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # presentation-ready text

# -----------------------------
# 2. Generate synthetic data
# -----------------------------
np.random.seed(42)
n_customers = 200

# Customer Acquisition Cost (CAC) in USD
cac = np.clip(np.random.normal(150, 50, n_customers), 50, 300)

# Customer Lifetime Value (CLV) in USD
clv = np.clip(2 * cac + np.random.normal(0, 50, n_customers), 50, 700)

# Create DataFrame
data = pd.DataFrame({"CAC": cac, "CLV": clv})

# -----------------------------
# 3. Create figure (exact 512x512 px)
# -----------------------------
fig, ax = plt.subplots(figsize=(512/100, 512/100), dpi=100)  # 5.12 x 5.12 inches @ 100 dpi

# Scatterplot
sns.scatterplot(
    data=data,
    x="CAC",
    y="CLV",
    color="dodgerblue",
    s=100,
    edgecolor="w",
    alpha=0.8,
    ax=ax
)

# Regression line
sns.regplot(
    data=data,
    x="CAC",
    y="CLV",
    scatter=False,
    color="orange",
    line_kws={"linewidth":2, "linestyle":"--"},
    ax=ax
)

# Titles and labels
ax.set_title("Customer Lifetime Value vs Acquisition Cost", fontsize=16, weight='bold')
ax.set_xlabel("Customer Acquisition Cost (USD)", fontsize=14)
ax.set_ylabel("Customer Lifetime Value (USD)", fontsize=14)

# Remove margins to ensure exact 512x512 px
ax.set_position([0, 0, 1, 1])  # full canvas
fig.canvas.draw()  # render everything

# -----------------------------
# 4. Save figure
# -----------------------------
fig.savefig("chart.png", dpi=100)  # exactly 512x512 pixels
plt.close()
