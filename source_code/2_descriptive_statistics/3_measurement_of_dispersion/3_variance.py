data = [2, 4, 6]

mean = sum(data) / len(data)

deviations = [x - mean for x in data]

squared = [d ** 2 for d in deviations]

variance = sum(squared) / len(data)

print(deviations)                 # [-2.0, 0.0, 2.0]​

print(squared)                    # [4.0, 0.0, 4.0]​

print(round(variance, 2))         # 2.67​


import statistics

print(round(statistics.pvariance(data), 2))  # 2.67​