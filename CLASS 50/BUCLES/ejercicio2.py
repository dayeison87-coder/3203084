class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

productos = [
    Producto("Laptop", 2500),
    Producto("Mouse", 50),
    Producto("Teclado", 120)
]

while True:   # bucle while
    nombre = input("Buscar producto (o escribir 'salir'): ")
    if nombre.lower() == "salir":
        break
    encontrado = False
    for p in productos:
        if p.nombre.lower() == nombre.lower():
            print(f"{p.nombre} - ${p.precio}")
            encontrado = True
    if not encontrado:
        print("Producto no encontrado")
