# Two students who know both, WITHOUT replacement​

p_first  = 8 / 40
p_second = 7 / 39        # one “both” student is already gone​

print(round(p_first * p_second, 4))   # 0.0359​

# Wrong: pretending the draws are independent​
print(round((8/40) ** 2, 4))          # 0.04​