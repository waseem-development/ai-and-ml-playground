import numpy as np
# Two heads in a row (independent)​

print(0.5 * 0.5)                  # 0.25​
# A 6 on a die, then a student who knows both​

print(round((1/6) * (8/40), 4))   # 0.0333​

# Check the first one by simulation​

rng = np.random.default_rng(1)

a = rng.integers(0, 2, 100_000)

b = rng.integers(0, 2, 100_000)

print(((a + b) == 2).mean())      # 0.24955​