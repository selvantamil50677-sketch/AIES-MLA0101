a, b = 0, 0
while a != 2:
    if b == 0:
        b = 3
    elif a == 4:
        a = 0
    else:
        x = min(b, 4 - a)
        a, b = a + x, b - x
    print("4L:", a, "3L:", b)
print("Goal reached")
