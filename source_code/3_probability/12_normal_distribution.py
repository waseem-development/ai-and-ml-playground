import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 1. Theoretical Model (Standard Normal Distribution: mean=0, std=1)
z = stats.norm(loc=0, scale=1)

print("--- Theoretical Probabilities (Empirical Rule) ---")
print("P(-1 <= Z <= 1) [within 1 std]:", round(z.cdf(1) - z.cdf(-1), 3))   # 0.683
print("P(-2 <= Z <= 2) [within 2 std]:", round(z.cdf(2) - z.cdf(-2), 3))   # 0.954
print("P(-3 <= Z <= 3) [within 3 std]:", round(z.cdf(3) - z.cdf(-3), 3))   # 0.997

# 2. Empirical Simulation (Sample 100,000 points from N(0, 1))
num_samples = 100_000
rng = np.random.default_rng(42)
samples = rng.normal(loc=0, scale=1, size=num_samples)

# Calculate empirical probabilities from simulated data
within_1std = np.mean((samples >= -1) & (samples <= 1))
within_2std = np.mean((samples >= -2) & (samples <= 2))
within_3std = np.mean((samples >= -3) & (samples <= 3))

print("\n--- Empirical Probabilities (100,000 Samples) ---")
print("P(-1 <= Z <= 1):", round(within_1std, 3))
print("P(-2 <= Z <= 2):", round(within_2std, 3))
print("P(-3 <= Z <= 3):", round(within_3std, 3))

# 3. Visualization: Theoretical PDF vs Empirical Histogram
x = np.linspace(-4, 4, 1000)
pdf = z.pdf(x)

plt.figure(figsize=(10, 5))

# Plot normalized empirical histogram
plt.hist(samples, bins=60, density=True, alpha=0.5, color='salmon', edgecolor='white', label=f'Empirical ({num_samples:,} samples)')

# Plot theoretical PDF curve
plt.plot(x, pdf, color='steelblue', lw=2.5, label='Theoretical PDF ($N(0,1)$)')

# Highlight 1, 2, 3 standard deviations
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for i, std in enumerate([1, 2, 3]):
    plt.axvline(std, color='gray', linestyle='--', alpha=0.7)
    plt.axvline(-std, color='gray', linestyle='--', alpha=0.7)

plt.title('Standard Normal Distribution $Z \sim \mathcal{N}(0,1)$ with Empirical Rule Shading')
plt.xlabel('Z-Score (Standard Deviations from Mean)')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()