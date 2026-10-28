father = {"Ravi": "Arun"}
mother = {"Ravi": "Meena"}
name = input("Enter child name:")
print("Father:", father.get(name, "Unknown"))
print("Mother:", mother.get(name, "Unknown"))
