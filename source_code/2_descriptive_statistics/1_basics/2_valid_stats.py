import statistics

colors = ["red", "blue", "red", "green"]  # Nominal
sizes = [1, 2, 2, 3, 4]                   # Ordinal
temps = [20, 25, 30]                      # Interval
income = [20, 40]                         # Ratio

print("Nominal → Most common color:", statistics.mode(colors))
print("Ordinal → Middle value of sizes:", statistics.median(sizes))
print("Interval → Average temperature:", statistics.mean(temps))
print("Ratio → $40 is", income[1] / income[0], "times $20")