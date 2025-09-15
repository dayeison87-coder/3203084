dic = {"Mercurio": 1, "Venus": 2, "Tierra": 3, "Marte": 4}
planeta = input("Ingrese planeta: ")
print("Su posición desde el sol es:", dic.get(planeta, "No encontrado"))
