from datetime import datetime
import uuid

class Usuario:
    def __init__(self, nombre, email):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.email = email
        self.direcciones = []

    def agregar_direccion(self, direccion):
        self.direcciones.append(direccion)

class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)

    def reducir_stock(self, cantidad):
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock -= cantidad

class Carrito:
    def __init__(self, usuario):
        self.usuario = usuario
        self.items = {}

    def agregar(self, producto, cantidad=1):
        if producto.id in self.items:
            self.items[producto.id] = (producto, self.items[producto.id][1] + cantidad)
        else:
            self.items[producto.id] = (producto, cantidad)

    def quitar(self, producto_id, cantidad=1):
        if producto_id not in self.items:
            return
        prod, cant = self.items[producto_id]
        nuevo = cant - cantidad
        if nuevo <= 0:
            del self.items[producto_id]
        else:
            self.items[producto_id] = (prod, nuevo)

    def total(self):
        return sum(prod.precio * cant for prod, cant in self.items.values())

    def vaciar(self):
        self.items = {}

class Orden:
    def __init__(self, usuario, carrito, direccion_envio):
        self.id = str(uuid.uuid4())
        self.usuario = usuario
        self.items = [(prod, cant) for prod, cant in carrito.items.values()]
        self.total = carrito.total()
        self.direccion = direccion_envio
        self.estado = "CREADA"
        self.fecha = datetime.now()

    def confirmar(self):
       
        for prod, cant in self.items:
            prod.reducir_stock(cant)
        self.estado = "CONFIRMADA"

    def cancelar(self):
        self.estado = "CANCELADA"

class Pago:
    def __init__(self, orden):
        self.id = str(uuid.uuid4())
        self.orden = orden
        self.estado = "PENDIENTE"
        self.detalle = None

    def pagar_con_tarjeta(self, numero, cvv, fecha_vencimiento):

        if len(str(numero)) < 12:
            self.estado = "FALLIDO"
            self.detalle = "Número inválido"
            return False
        self.estado = "APROBADO"
        self.detalle = f"Tarjeta terminada en {str(numero)[-4:]}"
        self.orden.confirmar()
        return True

    def pagar_con_paypal(self, cuenta_email):

        if "@" not in cuenta_email:
            self.estado = "FALLIDO"
            self.detalle = "Cuenta PayPal inválida"
            return False
        self.estado = "APROBADO"
        self.detalle = f"PayPal: {cuenta_email}"
        self.orden.confirmar()
        return True

    def pagar_efectivo(self):

        self.estado = "POR_RECOLECTAR"
        self.detalle = "Pago en efectivo (contra entrega)"
        self.orden.estado = "EN_PROCESO"
        return True

if __name__ == "__main__":
    u = Usuario("Ana", "ana@mail.com")
    p1 = Producto("Camiseta", 25.0, stock=10)
    p2 = Producto("Taza", 8.5, stock=5)

    cart = Carrito(u)
    cart.agregar(p1, 2)
    cart.agregar(p2, 1)
    print("Total carrito:", cart.total())

    orden = Orden(u, cart, "Calle Falsa 123")
    pago = Pago(orden)
    ok = pago.pagar_con_tarjeta(1234567812345678, 123, "12/27")
    print("Pago aprobado:", ok, "Estado pago:", pago.estado, "Estado orden:", orden.estado)
