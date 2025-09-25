class ProductoCarrito:
    def __init__(self, nombre, precio_unitario, cantidad=1, descuento=0):
        """
        descuento: porcentaje de descuento (ejemplo: 0.10 = 10%)
        """
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.descuento = descuento

    def subtotal(self):
        precio_bruto = self.precio_unitario * self.cantidad
        descuento_aplicado = precio_bruto * self.descuento
        return precio_bruto - descuento_aplicado

    def __str__(self):
        return (f"{self.nombre} x{self.cantidad} "
                f"(${self.precio_unitario:.2f} c/u, desc: {self.descuento*100:.0f}%) "
                f"=> Subtotal: ${self.subtotal():.2f}")



class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        return sum(p.subtotal() for p in self.productos)

    def mostrar_resumen(self):
        print("=== Carrito de Compras ===")
        for p in self.productos:
            print(p)
        print(f"TOTAL A PAGAR: ${self.calcular_total():.2f}")
        print("===========================")


if __name__ == "__main__":
    carrito = CarritoCompras()

    carrito.agregar_producto(ProductoCarrito("Laptop", 3000, cantidad=1, descuento=0.15))
    carrito.agregar_producto(ProductoCarrito("Mouse", 50, cantidad=2, descuento=0.10))
    carrito.agregar_producto(ProductoCarrito("Teclado", 100, cantidad=1, descuento=0))

    carrito.mostrar_resumen()
