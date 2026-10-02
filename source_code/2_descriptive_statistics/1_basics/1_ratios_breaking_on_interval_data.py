celsius = [20, 40]

fahrenheit = [c * 9 / 5 + 32 for c in celsius]

print("20°C and 40°C become:", fahrenheit)
print()
print("40°C / 20°C =", celsius[1] / celsius[0])
print("So, in Celsius, 40°C looks like 2 times 20°C")
print()
ratio_f = fahrenheit[1] / fahrenheit[0]

print("104°F / 68°F =", round(ratio_f, 4))
print("But in Fahrenheit, 104°F is NOT 2 times 68°F")
print()

# Ratio data (money) survives unit changes

usd = [20, 40]

print("$40 / $20 =", usd[1] / usd[0])
print("So, $40 is genuinely 2 times $20")