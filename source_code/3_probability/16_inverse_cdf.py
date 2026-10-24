"""
16_inverse_cdf.py  -  Inverse transform sampling

Goal: create fake (simulated) Golden Retriever weights that follow
a normal distribution, using only uniform random numbers.

Steps:
  1. Pick a random number u between 0 and 1 (uniform).
  2. Treat u as a cumulative probability.
  3. Use the inverse CDF (norm.ppf) to find the weight x where CDF(x) = u.
Repeat many times. The weights will follow the normal distribution.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mean, std_dev = 64.43, 2.99
n = 1000

rng = np.random.default_rng(42)   # fixed seed so results repeat every run

# Step 1: uniform random numbers (avoid exactly 0, which would give -infinity)
u = rng.uniform(1e-9, 1.0, size=n)

# Steps 2 and 3: inverse CDF turns each u into a weight
simulated_weights = norm.ppf(u, loc=mean, scale=std_dev)

# ---------------------------------------------------------------
# Print a check: do the simulated numbers match the theory?
# ---------------------------------------------------------------
print("First 5 examples (u -> weight):")
for ui, wi in zip(u[:5], simulated_weights[:5]):
    print(f"  u = {ui:.3f}  ->  weight = {wi:.2f} lb")

print(f"\n{'':20s}{'Simulated':>10s}{'Theory':>10s}")
print(f"{'Mean (lb)':20s}{simulated_weights.mean():10.2f}{mean:10.2f}")
print(f"{'Std dev (lb)':20s}{simulated_weights.std():10.2f}{std_dev:10.2f}")

# ---------------------------------------------------------------
# Plot: 3 panels that show the whole story from left to right
# ---------------------------------------------------------------
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(17, 5))

# Panel 1: the random inputs are flat (uniform)
ax1.hist(u, bins=20, color='lightgray', edgecolor='black')
ax1.set_title('Step 1: random numbers u\n(flat, every value equally likely)')
ax1.set_xlabel('u (a probability from 0 to 1)')
ax1.set_ylabel('Count')

# Panel 2: the inverse CDF is the machine that converts u into a weight
p = np.linspace(0.001, 0.999, 500)
ax2.plot(p, norm.ppf(p, mean, std_dev), color='green', linewidth=2, label='Inverse CDF (norm.ppf)')
# Show 3 example conversions
for ex_u in [0.1, 0.5, 0.9]:
    ex_w = norm.ppf(ex_u, mean, std_dev)
    ax2.plot([ex_u, ex_u], [mean - 4 * std_dev, ex_w],
             color='gray', linestyle=':')
    ax2.plot([0, ex_u], [ex_w, ex_w], color='gray', linestyle=':')
    ax2.plot(ex_u, ex_w, 'o', color='red')
    ax2.annotate(f'u={ex_u} -> {ex_w:.1f} lb', xy=(ex_u, ex_w),
                 xytext=(ex_u + 0.03 if ex_u < 0.8 else ex_u - 0.30, ex_w - 1.5 if ex_u < 0.5 else ex_w - 2.5))
ax2.set_title('Step 2 and 3: inverse CDF\nturns each u into a weight')
ax2.set_xlabel('u (cumulative probability)')
ax2.set_ylabel('Weight (lb)')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper left')

# Panel 3: the result matches the normal curve
ax3.hist(simulated_weights, bins=30, density=True, alpha=0.6, color='skyblue',
         edgecolor='black', label=f'Simulated weights (n={n})')
xs = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 300)
ax3.plot(xs, norm.pdf(xs, mean, std_dev), 'r-', linewidth=2.5, label='Theoretical normal PDF')
ax3.axvline(mean, color='darkred', linestyle='--', label=f'Mean ({mean} lb)')
ax3.set_title('Result: weights follow the normal curve')
ax3.set_xlabel('Weight (lb)')
ax3.set_ylabel('Density')
ax3.set_ylim(0, 0.19)
ax3.grid(True, linestyle=':', alpha=0.6)
ax3.legend(loc='upper right', fontsize=9)

fig.suptitle('Simulating Golden Retriever Weights with the Inverse CDF', fontsize=14)
plt.tight_layout()
plt.show()