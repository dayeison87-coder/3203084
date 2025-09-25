class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pedidos = []

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.detalles = []
        self.estado = "Pendiente"
        cliente.pedidos.append(self)

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)

    def cambiar_estado(self, estado):
        self.estado = estado

class DetallePedido:
    def __init__(self, producto, cantidad, precio):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

    def subtotal(self):
        return self.cantidad * self.precio

# Ejemplo
c1 = Cliente("Laura")
pedido = Pedido(c1)
pedido.agregar_detalle(DetallePedido("Pizza", 2, 20))
pedido.agregar_detalle(DetallePedido("Refresco", 3, 5))
pedido.cambiar_estado("En camino")

print(f"Pedido de {c1.nombre}: Estado {pedido.estado}")
print("Total:", sum(d.subtotal() for d in pedido.detalles))
