age = int(input("Enter age:"))
bmi = float(input("Enter BMI:"))
if bmi < 18.5:
    print("High-calorie diet")
elif bmi < 25:
    print("Balanced diet")
else:
    print("Low-calorie diet")
