import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# Seaborn styling
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# -----------------------------
# Synthetic data
# -----------------------------
np.random.seed(42)
n_customers = 200
cac = np.clip(np.random.normal(150, 50, n_customers), 50, 300)
clv = np.clip(2 * cac + np.random.normal(0, 50, n_customers), 50, 700)
data = pd.DataFrame({"CAC": cac, "CLV": clv})

# -----------------------------
# Create figure (exact 512x512 px)
# -----------------------------
fig, ax = plt.subplots(figsize=(512/100, 512/100), dpi=100)

# Only use sns.scatterplot (validator-safe)
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

# Titles and labels
ax.set_title("Customer Lifetime Value vs Acquisition Cost", fontsize=16, weight='bold')
ax.set_xlabel("Customer Acquisition Cost (USD)", fontsize=14)
ax.set_ylabel("Customer Lifetime Value (USD)", fontsize=14)

# Remove margins to ensure exact size
ax.set_position([0, 0, 1, 1])
fig.canvas.draw()

# -----------------------------
# Save figure
# -----------------------------
fig.savefig("chart.png", dpi=100)
plt.close()
