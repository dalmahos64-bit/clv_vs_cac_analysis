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

# Figure size exactly as assignment instructions
plt.figure(figsize=(8, 8))  # 8x8 inches
sns.scatterplot(
    data=data,
    x="CAC",
    y="CLV",
    color="dodgerblue",
    s=100
)

plt.title("Customer Lifetime Value vs Acquisition Cost")
plt.xlabel("Customer Acquisition Cost (USD)")
plt.ylabel("Customer Lifetime Value (USD)")

# Save as PNG exactly as assignment expects
plt.savefig("chart.png", dpi=64)
plt.close()
