# No overlap: a 2 OR a 5 on one die​
p = 1/6 + 1/6

print(round(p, 3))                # 0.333​
# Overlap: FastAPI OR ML​

p_fast, p_ml, p_both = 28/40, 20/40, 8/40
p_or = p_fast + p_ml - p_both

print(round(p_or, 3))             # 1.0  (= 40/40)​