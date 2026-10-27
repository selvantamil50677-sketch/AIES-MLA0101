import math

x = float(input("Enter input: "))
w = 0.5
b = 0.2

y = 1 / (1 + math.exp(-(x * w + b)))

print("Prediction:", round(y))
