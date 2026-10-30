dob = {
    "Arun": "12-05-2004",
    "Ravi": "10-08-2002"
}
name = input("Enter name: ")
print("Date of birth:", dob.get(name, "Not Found"))
