# P(event) = favorable / total​

die = [1, 2, 3, 4, 5, 6]
even = [x for x in die if x % 2 == 0]

p_even = len(even) / len(die)
print(p_even)                     # 0.5​

# complement rule: P(not A) = 1 - P(A)​
print(1 - p_even)                 # 0.5​