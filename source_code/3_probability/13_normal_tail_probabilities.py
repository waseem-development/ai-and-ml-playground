import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 1. Theoretical Model (IQ Score Distribution: mean=100, std=15)
mu, sigma = 100, 15
iq = stats.norm(loc=mu, scale=sigma)

print("--- Theoretical IQ Probabilities & Percentiles ---")
print("P(IQ > 130) [Right Tail]:", round(1 - iq.cdf(130), 4))  # 0.0228 (Top ~2.3%)
print("P(IQ < 85)  [Left Tail] :", round(iq.cdf(85), 4))       # 0.1587 (Bottom ~15.9%)

# Percent Point Function (PPF) - Inverse CDF
# What IQ score marks the top 2.5%? (i.e., 97.5th percentile)
top_2_5_cutoff = round(iq.ppf(0.975), 1)
print(f"Top 2.5% Cutoff (97.5th Percentile): IQ {top_2_5_cutoff}")  # 129.4


# 2. Empirical Simulation (100,000 Simulated IQ Scores)
num_samples = 100_000
rng = np.random.default_rng(42)
simulated_iqs = rng.normal(loc=mu, scale=sigma, size=num_samples)

empirical_right_tail = np.mean(simulated_iqs > 130)
empirical_left_tail = np.mean(simulated_iqs < 85)
empirical_97_5_percentile = np.percentile(simulated_iqs, 97.5)

print("\n--- Empirical Results (100,000 Samples) ---")
print("Empirical P(IQ > 130):", round(empirical_right_tail, 4))
print("Empirical P(IQ < 85) :", round(empirical_left_tail, 4))
print(f"Empirical 97.5th Percentile Cutoff: IQ {round(empirical_97_5_percentile, 1)}")


# 3. Visualization of Probability Tails
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
pdf = iq.pdf(x)

plt.figure(figsize=(10, 5))

# Plot full PDF curve
plt.plot(x, pdf, color='black', lw=2, label='IQ Normal Distribution $\mathcal{N}(100, 15^2)$')

# Shade Left Tail: IQ < 85
x_left = np.linspace(mu - 4 * sigma, 85, 200)
plt.fill_between(x_left, iq.pdf(x_left), color='coral', alpha=0.6, label='Left Tail: P(IQ < 85) = 15.87%')

# Shade Right Tail: IQ > 130
x_right = np.linspace(130, mu + 4 * sigma, 200)
plt.fill_between(x_right, iq.pdf(x_right), color='mediumpurple', alpha=0.6, label='Right Tail: P(IQ > 130) = 2.28%')

# Add threshold lines
plt.axvline(100, color='gray', linestyle='--', alpha=0.7, label='Mean (IQ = 100)')
plt.axvline(85, color='coral', linestyle=':', lw=2)
plt.axvline(130, color='mediumpurple', linestyle=':', lw=2)

plt.title('Normal Distribution Probability Tails (IQ Scale)')
plt.xlabel('IQ Score')
plt.ylabel('Probability Density')
plt.xticks([55, 70, 85, 100, 115, 130, 145])
plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()