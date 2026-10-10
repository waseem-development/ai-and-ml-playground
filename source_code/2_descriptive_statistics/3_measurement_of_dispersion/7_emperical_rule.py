import numpy as np

from scipy import stats


rng = np.random.default_rng(1)

x = rng.normal(0, 1, 100_000)


def within(k):

    return round(float(np.mean(np.abs(x) < k)), 3)


print(within(1))                  # 0.684​

print(within(2))                  # 0.955​

print(within(3))                  # 0.997​ ​

