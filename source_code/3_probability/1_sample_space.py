import itertools

dice = list(itertools.product(range(1, 7), repeat=2))

print(len(dice))                  # 36​

sum7 = [d for d in dice if sum(d) == 7]

print(len(sum7))                  # 6​

print(round(len(sum7) / len(dice), 4))   # 0.1667​