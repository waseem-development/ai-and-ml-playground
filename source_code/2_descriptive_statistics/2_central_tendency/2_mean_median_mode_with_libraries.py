import statistics
import numpy as np
import pandas as pd
from scipy import stats as st
 
data = pd.Series([4, 8, 6, 5, 3, 8, 9])
 
print(statistics.mean(data))      # 6.142857142857143
print(np.median(data))            # 6.0
print(pd.Series(data).mode()[0])  # 8
print(st.mode(data).mode)      # 8
print(statistics.multimode([1, 1, 2, 2, 3]))  # [1, 2]  