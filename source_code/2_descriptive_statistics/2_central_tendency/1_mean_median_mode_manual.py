data = [4, 8, 6, 5, 3, 8, 9]
 
mean = sum(data) / len(data)
 
s = sorted(data)
mid = len(s) // 2
median = (s[mid] if len(s) % 2 else (s[mid-1] + s[mid]) / 2)
 
mode = max(set(data), key=data.count)
 
print(round(mean, 2))             # 6.14
print(median)                     # 6
print(mode)                       # 8