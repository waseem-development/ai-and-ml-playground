import numpy as np

from scipy import stats

hours = [1, 2, 3, 4, 5, 6]

score = [52, 55, 61, 64, 70, 74]

print(round(np.corrcoef(hours, score)[0, 1], 3))

# → 0.996​

r, p = stats.pearsonr(hours, score)

print(round(r, 3))                # 0.996​

x = [-3, -2, -1, 0, 1, 2, 3]

y = [v ** 2 for v in x]           # perfect curve​

print(round(np.corrcoef(x, y)[0, 1], 2))  # 0.0​