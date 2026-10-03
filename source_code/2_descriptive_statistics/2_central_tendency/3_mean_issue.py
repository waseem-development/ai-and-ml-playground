import numpy as np
from scipy import stats

salaries = [40, 42, 45, 48, 500]  # in $k
print("Arithmetic mean of salaries:", np.mean(salaries))
print("Median salary:", np.median(salaries))
print("Bigger and smaller values trimmed mean of salaries:", stats.trim_mean(salaries, 0.2))
# Weighted mean: exam is worth 3× the quiz
print("Weighted mean of quiz and exam scores:", 
      np.average([80, 90], weights=[1, 3]))