class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        if porcentaje > 0 and porcentaje <= 50:
            self.precio -= self.precio * (porcentaje / 100)
            return f"Nuevo precio de {self.nombre}: {self.precio}"
        else:
            return "Descuento no válido."

p = Producto("Celular", 1000)
print(p.aplicar_descuento(20))
