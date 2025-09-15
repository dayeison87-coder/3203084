dic = {"Manzana": 1500, "Pera": 1200, "Banano": 1000, "Mango": 2000}
fruta = input("Ingrese una fruta: ")
print("Precio:", dic.get(fruta, "No disponible"))
