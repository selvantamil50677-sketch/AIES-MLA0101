x = [0, 1, 0, 1]
y = [0, 1, 0, 1]
for a, b in zip(x, y):
    print("Disease:", "Yes" if a == b == 1 else "No")
