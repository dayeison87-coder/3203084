dic = {"Hamburguesa": 15000, "Perro caliente": 10000, "Pizza": 20000, "Tacos": 18000}
pedido = input("Ingrese su comida: ")
print("Precio:", dic.get(pedido, "No disponible"))
