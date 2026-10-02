import numpy as np

rng = np.random.default_rng(1)
pop = rng.normal(70, 10, 10_000) 

"""
70      → Mean
10      → Standard deviation
10,000  → Number of values
"""

random_sample = rng.choice(pop, 200)
biased_sample = pop[pop > 75][:1000]

print("True population mean:", round(pop.mean(), 1))
print("Mean of random sample:", round(random_sample.mean(), 1))
print("Mean of biased sample:", round(biased_sample.mean(), 1))