class Banco:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        return f"Depositaste {cantidad}. Saldo actual: {self.saldo}"

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Retiraste {cantidad}. Saldo actual: {self.saldo}"
        else:
            return "Fondos insuficientes."

b = Banco(1000)
print(b.depositar(500))
print(b.retirar(1200))
