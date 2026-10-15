import numpy as np

rng = np.random.default_rng(7)
flips = rng.integers(0, 2, size=10_000)  # 1 = heads​

for n in [10, 100, 1000, 10_000]:

    print(n, flips[:n].mean())