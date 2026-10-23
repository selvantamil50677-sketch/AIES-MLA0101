values = [3, 5, 2, 9]
left = min(values[0], values[1])
if left <= 3:
    right = min(values[2], values[3])
print("Best values:", max(left, right))
