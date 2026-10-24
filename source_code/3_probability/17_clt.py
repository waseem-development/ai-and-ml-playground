"""
17_clt.py  -  The Central Limit Theorem (CLT)

Big idea:
  Take many random samples from ANY population (even a very skewed one).
  Calculate the mean of each sample.
  Those sample means form a NORMAL distribution, and it gets more normal
  as the sample size n grows.

Also:
  mean of the sample means = population mean (mu)
  std dev of the sample means = sigma / sqrt(n)   (called the "standard error")

Example: waiting time (in minutes) for a bus. Most buses come quickly,
but a few take a very long time. This is a skewed (exponential) population,
nothing like a bell curve.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, skew

rng = np.random.default_rng(42)   # fixed seed so results repeat every run

# ---------------------------------------------------------------
# 1. The population: exponential (skewed, NOT normal)
# ---------------------------------------------------------------
scale = 2.0          # for an exponential, mean = scale and std dev = scale
mu = scale           # population mean
sigma = scale        # population std dev

population = rng.exponential(scale, size=100_000)
print(f"Population: mean = {population.mean():.2f} (theory {mu}), "
      f"std dev = {population.std():.2f} (theory {sigma})")
print(f"Population skewness = {skew(population):.2f}  (0 means perfectly symmetric)\n")

# ---------------------------------------------------------------
# 2. Draw many samples for different sample sizes n
#    For each n: take 10,000 samples of size n, and keep the mean of each
# ---------------------------------------------------------------
sample_sizes = [1, 2, 5, 30]
n_samples = 10_000
sample_means = {}

for n in sample_sizes:
    draws = rng.exponential(scale, size=(n_samples, n))   # 10,000 rows, n columns
    sample_means[n] = draws.mean(axis=1)                  # one mean per row

# ---------------------------------------------------------------
# 3. Print a check: do the results match the CLT formulas?
# ---------------------------------------------------------------
print(f"{'n':>4}{'Mean of means':>16}{'Theory (mu)':>14}"
      f"{'Std of means':>15}{'Theory (s/sqrt n)':>19}{'Skewness':>10}")
for n in sample_sizes:
    m = sample_means[n]
    print(f"{n:>4}{m.mean():>16.3f}{mu:>14.3f}"
          f"{m.std():>15.3f}{sigma / np.sqrt(n):>19.3f}{skew(m):>10.2f}")
print("\nSkewness moves toward 0 as n grows: the shape becomes symmetric (normal).")

# ---------------------------------------------------------------
# 4. Plot
#    Top: the skewed population
#    Bottom: the sample means for n = 1, 2, 5, 30 with the CLT curve on top
# ---------------------------------------------------------------
fig = plt.figure(figsize=(15, 9))
grid = fig.add_gridspec(2, 4)

# --- Top: population ---
ax_pop = fig.add_subplot(grid[0, :])
ax_pop.hist(population, bins=80, range=(0, 14), density=True, color='lightgray', edgecolor='black')
ax_pop.axvline(mu, color='red', linestyle='--', linewidth=2, label=f'Population mean ({mu} min)')
ax_pop.set_title('The population: bus waiting times (skewed, NOT a bell curve)')
ax_pop.set_xlabel('Waiting time (minutes)')
ax_pop.set_ylabel('Density')
ax_pop.grid(True, linestyle=':', alpha=0.6)
ax_pop.legend()

# --- Bottom: sample means ---
colors = ['lightcoral', 'khaki', 'lightgreen', 'skyblue']
for i, n in enumerate(sample_sizes):
    ax = fig.add_subplot(grid[1, i])
    m = sample_means[n]
    se = sigma / np.sqrt(n)    # the CLT says the std dev of the means is this

    ax.hist(m, bins=40, density=True, color=colors[i], edgecolor='black', alpha=0.8,
            label='Sample means')

    # The normal curve the CLT predicts: mean = mu, std dev = sigma / sqrt(n)
    xs = np.linspace(max(0, mu - 4 * se), mu + 4 * se, 300)
    ax.plot(xs, norm.pdf(xs, mu, se), 'r-', linewidth=2.5, label='Normal curve from CLT')
    ax.axvline(mu, color='darkred', linestyle='--', linewidth=1.5)

    ax.set_title(f'Sample size n = {n}\nstd error = {se:.2f}, skewness = {skew(m):.2f}')
    ax.set_xlabel('Sample mean (minutes)')
    if i == 0:
        ax.set_ylabel('Density')
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper right', fontsize=8)

fig.suptitle('Central Limit Theorem: means of a skewed population become normal as n grows',
             fontsize=14)
plt.tight_layout()
plt.show()