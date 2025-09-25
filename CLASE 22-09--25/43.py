class Producto:
    def _init_(self, id, nombre, stock=0):
        self.id = id
        self.nombre = nombre
        self.stock = stock


class Proveedor:
    def _init_(self, nombre):
        self.nombre = nombre

    def suministrar(self, producto, cantidad):
        producto.stock += cantidad


class Orden:
    def _init_(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad


class Almacen:
    def _init_(self):
        self.productos = {}

    def add_producto(self, producto):
        self.productos[producto.id] = producto

    def predecir_baja(self, id):
        p = self.productos.get(id)
        return p and p.stock < 5


# ejemplo
alm = Almacen()
cafe = Producto(1, "Café", 3)
alm.add_producto(cafe)
print("¿Reabastecer?", alm.predecir_baja(1))