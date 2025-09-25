class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"{self.titular} depositó ${monto:.2f}. Saldo actual: ${self.saldo:.2f}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if monto > 0 and self.saldo >= monto:
            self.saldo -= monto
            print(f"{self.titular} retiró ${monto:.2f}. Saldo actual: ${self.saldo:.2f}")
        else:
            print("Fondos insuficientes.")

    def mostrar_saldo(self):
        print(f"Saldo de {self.titular}: ${self.saldo:.2f}")

class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo=0, interes=0.02):
        super().__init__(titular, saldo)
        self.interes = interes 

    def aplicar_interes(self):
        ganancia = self.saldo * self.interes
        self.saldo += ganancia
        print(f"Intereses aplicados a {self.titular}: +${ganancia:.2f}. Saldo: ${self.saldo:.2f}")

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo=0, limite_sobregiro=500):
        super().__init__(titular, saldo)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto):
        if monto > 0 and self.saldo - monto >= -self.limite_sobregiro:
            self.saldo -= monto
            print(f"{self.titular} retiró ${monto:.2f}. Saldo actual: ${self.saldo:.2f}")
        else:
            print("No puedes superar el límite de sobregiro.")

if __name__ == "__main__":
  
    cuenta_ahorros = CuentaAhorros("Ana", 1000, interes=0.05)
    cuenta_corriente = CuentaCorriente("Carlos", 500, limite_sobregiro=300)

    cuenta_ahorros.depositar(500)
    cuenta_ahorros.aplicar_interes()
    cuenta_ahorros.retirar(200)
    cuenta_ahorros.mostrar_saldo()

    print("\n-----------------------------\n")

    cuenta_corriente.retirar(600)   
    cuenta_corriente.retirar(300)  
    cuenta_corriente.depositar(200)
    cuenta_corriente.mostrar_saldo()
