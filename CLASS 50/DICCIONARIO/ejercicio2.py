class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

productos = {
    "Laptop": {"objeto": Producto("Laptop", 2500), "cantidad": 5},
    "Mouse": {"objeto": Producto("Mouse", 50), "cantidad": 20},
    "Teclado": {"objeto": Producto("Teclado", 120), "cantidad": 10}
}

for nombre, datos in productos.items():  # ciclo for
    p = datos["objeto"]
    print(f"{p.nombre} - ${p.precio} - Stock: {datos['cantidad']}")
