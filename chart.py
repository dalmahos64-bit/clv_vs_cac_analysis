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
cac = np.random.normal(loc=150, scale=50, size=n_customers)
cac = np.clip(cac, 50, 300)  # realistic range

# Customer Lifetime Value (CLV) in USD
clv = 2 * cac + np.random.normal(loc=0, scale=50, size=n_customers)
clv = np.clip(clv, 50, 700)

# Create DataFrame
data = pd.DataFrame({"CAC": cac, "CLV": clv})

# -----------------------------
# 3. Create scatterplot
# -----------------------------
plt.figure(figsize=(8, 8))  # 512x512 pixels at 64 dpi
scatter = sns.scatterplot(
    data=data,
    x="CAC",
    y="CLV",
    palette="viridis",
    s=100,
    color="dodgerblue",
    edgecolor="w",
    alpha=0.8
)

# Add titles and labels
plt.title("Customer Lifetime Value vs Acquisition Cost", fontsize=16, weight='bold')
plt.xlabel("Customer Acquisition Cost (USD)", fontsize=14)
plt.ylabel("Customer Lifetime Value (USD)", fontsize=14)

# Optional: add regression line
sns.regplot(
    data=data,
    x="CAC",
    y="CLV",
    scatter=False,
    color="orange",
    line_kws={"linewidth":2, "linestyle":"--"}
)

# -----------------------------
# 4. Save the chart
# -----------------------------
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches='tight')  # 512x512 pixels
plt.close()
