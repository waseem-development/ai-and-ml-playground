import numpy as np

from scipy import stats

data = [10, 12, 14, 15, 16, 18, 20, 95]
q1, q3 = np.percentile(data, [25, 75])

print(q3 - q1)                    # 5.0​

print(stats.iqr(data))            # 5.0​

print(round(np.std(data), 1))     # 26.6​

print(round(np.std(data[:-1]), 1))  # 3.2​