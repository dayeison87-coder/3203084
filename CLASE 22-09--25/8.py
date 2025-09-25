class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, porcentaje):
        if 0 < porcentaje < 100:
            descuento = self.precio * (porcentaje / 100)
            self.precio -= descuento
            print(f"Descuento aplicado. Nuevo precio: {self.precio:.2f}")
        else:
            print("Porcentaje de descuento inválido.")


prod = Producto("A001", "maleta", 50000, 10)
print(f"Precio original: {prod.precio}")
prod.aplicar_descuento(20)
print(f"Precio con descuento: {prod.precio}")