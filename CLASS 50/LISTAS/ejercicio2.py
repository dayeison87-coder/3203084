class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

productos = [
    Producto("Laptop", 2500),
    Producto("Mouse", 50),
    Producto("Teclado", 120),
    Producto("Monitor", 800)
]

print("Inventario:")
for p in productos:
    print(f"{p.nombre} - ${p.precio}")

mas_caro = max(productos, key=lambda x: x.precio)
mas_barato = min(productos, key=lambda x: x.precio)

print(f"\nProducto más caro: {mas_caro.nombre} - ${mas_caro.precio}")
print(f"Producto más barato: {mas_barato.nombre} - ${mas_barato.precio}")
