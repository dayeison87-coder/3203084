ciudades = []
for i in range(10):
    ciudades.append(input(f"Ciudad {i+1}: "))
for i, c in enumerate(ciudades, 1):
    print(f"{i}. {c}")