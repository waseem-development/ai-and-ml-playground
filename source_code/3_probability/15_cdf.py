"""
15_cdf.py  -  The Cumulative Distribution Function (CDF)

Example: weights of adult Golden Retrievers (in lb).

Big idea:
  CDF(x) = probability that a weight is LESS THAN OR EQUAL to x.
  It is the area under the PDF from far left up to x.
  So the probability between a and b is:  CDF(b) - CDF(a)
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mean, std_dev = 64.43, 2.99
a, b = 62, 66   # the weight range we care about

# ---------------------------------------------------------------
# 1. Print results with clear explanations
# ---------------------------------------------------------------
cdf_mean = norm.cdf(mean, mean, std_dev)
print(f"P(weight <= {mean})  = {cdf_mean:.4f}  (half the dogs weigh less than the mean)")

cdf_a = norm.cdf(a, mean, std_dev)
cdf_b = norm.cdf(b, mean, std_dev)
prob = cdf_b - cdf_a
print(f"P(weight <= {a})     = {cdf_a:.4f}")
print(f"P(weight <= {b})     = {cdf_b:.4f}")
print(f"P({a} < weight < {b}) = {cdf_b:.4f} - {cdf_a:.4f} = {prob:.4f}  (about {prob * 100:.1f}%)")

# ---------------------------------------------------------------
# 2. Plot: PDF on the left, CDF on the right
# ---------------------------------------------------------------
x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 500)
pdf = norm.pdf(x, mean, std_dev)
cdf = norm.cdf(x, mean, std_dev)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# --- Left: PDF with the shaded area ---
ax1.plot(x, pdf, color='blue', linewidth=2, label='PDF')
x_fill = np.linspace(a, b, 200)
ax1.fill_between(x_fill, norm.pdf(x_fill, mean, std_dev), color='skyblue', alpha=0.7,
                 label=f'Area between {a} and {b} = {prob:.3f}')
ax1.axvline(mean, color='red', linestyle='--', label=f'Mean ({mean} lb)')
ax1.text((a + b) / 2, norm.pdf(mean, mean, std_dev) * 0.35, f'{prob * 100:.1f}%',
         ha='center', fontsize=14, fontweight='bold')
ax1.set_title('PDF: the shaded AREA is the probability')
ax1.set_xlabel('Weight (lb)')
ax1.set_ylabel('Probability density')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper right', fontsize=9)

# --- Right: CDF with the two heights and the gap between them ---
ax2.plot(x, cdf, color='green', linewidth=2, label='CDF')
for point, value in [(a, cdf_a), (b, cdf_b)]:
    ax2.plot([point, point], [0, value], color='gray', linestyle=':')
    ax2.plot([x[0], point], [value, value], color='gray', linestyle=':')
    ax2.plot(point, value, 'o', color='black')
    ax2.annotate(f'CDF({point}) = {value:.3f}', xy=(point, value),
                 xytext=(point + (1.2 if point == b else -7.5), value + (-0.12 if point == b else 0.06)),
                 arrowprops=dict(arrowstyle='->'))

# Show the gap between the two heights
ax2.annotate('', xy=(b + 0.4, cdf_b), xytext=(b + 0.4, cdf_a),
             arrowprops=dict(arrowstyle='<->', color='red', linewidth=2))
ax2.text(b + 0.7, (cdf_a + cdf_b) / 2, f'gap = {prob:.3f}', color='red', va='center', fontweight='bold')

ax2.axhline(0.5, color='red', linestyle='--', alpha=0.5, label='0.5 at the mean')
ax2.set_title('CDF: probability = difference in HEIGHT')
ax2.set_xlabel('Weight (lb)')
ax2.set_ylabel('Cumulative probability  P(weight <= x)')
ax2.set_ylim(0, 1.05)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper left')

fig.suptitle('Golden Retriever Weights: PDF vs CDF', fontsize=14)
plt.tight_layout()
plt.show()