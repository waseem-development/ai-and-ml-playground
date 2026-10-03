import math

import statistics

import numpy as np



data = [2, 4, 6]

variance = statistics.pvariance(data)

print(round(math.sqrt(variance), 2))  # 1.63​

print(round(statistics.pstdev(data), 2))  # 1.63​

print(round(np.std(data), 2))     # 1.63​