dic = {"H": "Hidrógeno", "O": "Oxígeno", "C": "Carbono", "Na": "Sodio"}
simbolo = input("Ingrese símbolo químico: ")
print("Elemento:", dic.get(simbolo, "No encontrado"))
