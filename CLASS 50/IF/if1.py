class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return f"Retiro exitoso. Saldo actual: {self.saldo}"
        else:
            return "Fondos insuficientes."

c1 = CuentaBancaria(1000)
print(c1.retirar(500))