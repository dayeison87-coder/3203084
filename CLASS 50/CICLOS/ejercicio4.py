class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

productos = [
    Producto("Laptop", 2500),
    Producto("Mouse", 50),
    Producto("Teclado", 120)
]

i = 0
while i < len(productos):   # ciclo while
    if productos[i].precio > 100:
        print(f"{productos[i].nombre} cuesta más de 100")
    i += 1
