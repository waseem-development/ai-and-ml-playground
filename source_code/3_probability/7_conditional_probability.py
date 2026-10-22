# 20 FastAPI only (D), 12 ML only (M), 8 both (B)​

students = ["D"] * 20 + ["M"] * 12 + ["B"] * 8

# Given: the student knows FastAPI​

data = [s for s in students if s in ("D", "B")]
both = [s for s in data if s == "B"]

print(len(data), len(both))      # 28  8​

print(round(len(both) / len(data), 4))     # 0.2857​