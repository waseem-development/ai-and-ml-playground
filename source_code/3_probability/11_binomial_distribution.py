import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 1. Theoretical Model (Binomial Distribution: 10 coin flips, p=0.5)
n, p = 10, 0.5
heads = stats.binom(n=n, p=p)

print("--- Theoretical Statistics ---")
print("P(exactly 5 heads):", round(heads.pmf(5), 3))      # 0.246
print("P(at most 3 heads):", round(heads.cdf(3), 3))      # 0.172
print("P(8 or more heads):", round(1 - heads.cdf(7), 3))  # 0.055
print("Mean:", heads.mean())                             # 5.0
print("Standard Deviation:", round(heads.std(), 2))      # 1.58

# 2. Empirical Simulation (Simulate 10,000 trials of 10 coin flips each)
num_trials = 10_000
rng = np.random.default_rng(42)
simulated_heads = rng.binomial(n=n, p=p, size=num_trials)

# Count frequencies for each possible outcome (0 to 10 heads)
counts = np.bincount(simulated_heads, minlength=n+1)
empirical_probs = counts / num_trials

# 3. Compare Theoretical PMF vs. Empirical Frequencies
k_values = np.arange(0, n + 1)
theoretical_probs = heads.pmf(k_values)

# Plotting the comparison
plt.figure(figsize=(10, 4))
plt.bar(k_values - 0.15, theoretical_probs, width=0.3, label='Theoretical PMF', color='skyblue', edgecolor='black')
plt.bar(k_values + 0.15, empirical_probs, width=0.3, label=f'Empirical ({num_trials:,} trials)', color='salmon', edgecolor='black')

plt.xlabel('Number of Successes / Heads (k)')
plt.ylabel('Probability')
plt.title('Theoretical vs. Empirical Binomial Distribution (n=10, p=0.5)')
plt.xticks(k_values)
plt.ylim(0, 0.30)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()