import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 1. Theoretical Model (Discrete Uniform Distribution)
die = stats.randint(1, 7)         # faces 1 to 6 (upper bound is exclusive)

# 2. Perfect Uniform Simulation (Exact Equal Counts)
num_rolls = 6000
faces = np.arange(1, 7)

# Instead of random rolls, we force a perfectly even distribution
# Each face gets exactly num_rolls / 6 counts
counts = np.full(6, num_rolls // 6)
print(f"Perfect Counts across {num_rolls:,} rolls (faces 1-6):", counts)
# Output: [1000 1000 1000 1000 1000 1000]

# 3. Compare Theoretical PMF vs. Perfect Empirical Frequencies
empirical_probs = counts / num_rolls
theoretical_probs = die.pmf(faces)

# Plotting the comparison
plt.figure(figsize=(8, 4))
plt.bar(faces - 0.15, theoretical_probs, width=0.3, label='Theoretical PMF', color='skyblue', edgecolor='black')
plt.bar(faces + 0.15, empirical_probs, width=0.3, label=f'Perfect Uniform ({num_rolls:,} rolls)', color='mediumseagreen', edgecolor='black')

plt.xlabel('Die Face')
plt.ylabel('Probability')
plt.title('Perfect Uniform Distribution (Zero Random Variance)')
plt.xticks(faces)
plt.ylim(0, 0.20)  # Starts y-axis at 0 for proper visual proportion
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()