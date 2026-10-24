"""
14_pdf.py  -  The Probability Density Function (PDF) of a normal distribution

Example: weights of adult Golden Retrievers (in lb).

Big idea:
  The PDF height at a point is NOT a probability.
  It is a "density". Probability is the AREA under the curve.
  The total area under the whole curve is always 1 (100%).
"""
import math
import numpy as np
import matplotlib.pyplot as plt

mean = 64.43     # average weight (lb)
std_dev = 2.99   # how spread out the weights are (lb)


def normal_pdf(x, mean, std_dev):
    """Normal PDF written by hand from the formula."""
    return (1.0 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mean) / std_dev) ** 2)


# ---------------------------------------------------------------
# 1. Print some values so we can SEE what the function does
# ---------------------------------------------------------------
print("PDF height (density) at different weights:")
for w in [mean - 2 * std_dev, mean - std_dev, mean, mean + std_dev, mean + 2 * std_dev]:
    print(f"  weight = {w:6.2f} lb  ->  density = {normal_pdf(w, mean, std_dev):.4f}")

# ---------------------------------------------------------------
# 2. Check that the total area under the curve is about 1
#    (we add up many thin rectangles: height * width)
# ---------------------------------------------------------------
n_points = 2000
x_values = np.linspace(mean - 6 * std_dev, mean + 6 * std_dev, n_points)
y_values = np.array([normal_pdf(x, mean, std_dev) for x in x_values])
dx = x_values[1] - x_values[0]
total_area = np.sum(y_values * dx)
print(f"\nTotal area under the curve: {total_area:.4f}  (should be about 1.0)")

# ---------------------------------------------------------------
# 3. Area within 1, 2 and 3 standard deviations (the 68-95-99.7 rule)
# ---------------------------------------------------------------
print("\nThe 68-95-99.7 rule (area = probability):")
for k in [1, 2, 3]:
    mask = (x_values >= mean - k * std_dev) & (x_values <= mean + k * std_dev)
    area = np.sum(y_values[mask] * dx)
    print(f"  within {k} std dev ({mean - k * std_dev:.1f} to {mean + k * std_dev:.1f} lb): {area * 100:.1f}%")

# ---------------------------------------------------------------
# 4. Plot
# ---------------------------------------------------------------
x_plot = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 500)
y_plot = np.array([normal_pdf(x, mean, std_dev) for x in x_plot])

plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, color='black', linewidth=2, label='Normal PDF')

# Shade the three bands, widest first so the narrow ones sit on top
bands = [
    (3, 'lightgreen', 'Within 3 std dev (about 99.7%)'),
    (2, 'khaki',      'Within 2 std dev (about 95%)'),
    (1, 'skyblue',    'Within 1 std dev (about 68%)'),
]
for k, color, label in bands:
    xs = np.linspace(mean - k * std_dev, mean + k * std_dev, 200)
    ys = np.array([normal_pdf(x, mean, std_dev) for x in xs])
    plt.fill_between(xs, ys, color=color, alpha=0.8, label=label)

# Mark the peak
peak = normal_pdf(mean, mean, std_dev)
plt.axvline(mean, color='red', linestyle='--', linewidth=1.5)
plt.annotate(f'Peak (the mean)\n{mean} lb, density = {peak:.3f}',
             xy=(mean, peak), xytext=(mean + 2.2 * std_dev, peak * 0.95),
             arrowprops=dict(arrowstyle='->', color='red'), color='red')

# Mark the std dev positions on the x axis
ticks = [mean + k * std_dev for k in range(-3, 4)]
plt.xticks(ticks, [f'{t:.1f}\n({k:+d}σ)' if k != 0 else f'{t:.1f}\n(mean)'
                   for t, k in zip(ticks, range(-3, 4))])

plt.title('Normal Distribution PDF: Golden Retriever Weights\n'
          'Probability = AREA under the curve, not the height')
plt.xlabel('Weight (lb)')
plt.ylabel('Probability density')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()