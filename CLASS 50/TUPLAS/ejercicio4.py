class Producto:
    def __init__(self, nombre, precios):
        self.datos = (nombre, precios)

prod1 = Producto("Laptop", (2500, 2450, 2600))
prod2 = Producto("Mouse", (50, 55, 60))

for prod in (prod1, prod2):
    nombre, precios = prod.datos
    print(f"{nombre} - Precios: {precios} - Mínimo: {min(precios)}")
