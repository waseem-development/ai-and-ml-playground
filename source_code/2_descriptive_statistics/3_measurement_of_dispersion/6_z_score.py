import numpy as np

from scipy import stats

z = (86 - 70) / 8

print(z, "\n") # 2.0​

scores = [60, 65, 70, 75, 80]

print(stats.zscore(scores).round(2), "\n")

# → [-1.41 -0.71 0. 0.71 1.41]​

print(round(np.mean(stats.zscore(scores)), 2), "\n") # 0.0​
