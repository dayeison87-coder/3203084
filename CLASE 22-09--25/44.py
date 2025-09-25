import random

class Accion:
    def _init_(self, symbol, precio):
        self.symbol = symbol
        self.precio = precio

    def simular_cambio(self):
        self.precio *= 1 + (random.random() - 0.5) / 10


class Portafolio:
    def _init_(self):
        self.posiciones = {}

    def comprar(self, sym, cantidad):
        self.posiciones[sym] = self.posiciones.get(sym, 0) + cantidad


class Mercado:
    def _init_(self):
        self.lista = {}

    def agregar(self, accion):
        self.lista[accion.symbol] = accion

    def tick(self):
        for a in self.lista.values():
            a.simular_cambio()


# ejemplo
m = Mercado()
aapl = Accion("AAPL", 150)
m.agregar(aapl)
pf = Portafolio()
pf.comprar("AAPL", 10)
m.tick()
print("Precio AAPL:", round(m.lista["AAPL"].precio, 2))