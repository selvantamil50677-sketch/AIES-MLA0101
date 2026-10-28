planets = {
    "earth": "Third planet",
    "mars": "Fourth planet",
    "jupiter": "Largest planet"
}
name = input("Enter planet: ").lower()
print(planets.get(name, "Planet not found"))
