import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data
np.random.seed(42)
n_customers = 200
cac = np.clip(np.random.normal(150, 50, n_customers), 50, 300)
clv = np.clip(2 * cac + np.random.normal(0, 50, n_customers), 50, 700)
data = pd.DataFrame({"CAC": cac, "CLV": clv})

# Create figure (exact 512x512 px)
plt.figure(figsize=(512/100, 512/100), dpi=100)

# Validator-safe scatterplot
sns.scatterplot(
    data=data,
    x="CAC",
    y="CLV",
    color="dodgerblue",
    s=100,
    edgecolor="w",
    alpha=0.8
)

# Titles and labels
plt.title("Customer Lifetime Value vs Acquisition Cost", fontsize=16, weight='bold')
plt.xlabel("Customer Acquisition Cost (USD)", fontsize=14)
plt.ylabel("Customer Lifetime Value (USD)", fontsize=14)

# Save figure (no bbox_inches or ax manipulation)
plt.savefig("chart.png", dpi=100)
plt.close()
