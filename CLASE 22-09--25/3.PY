class CuentaBanco:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial  # saldo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print("Fondos insuficientes.")
        elif cantidad <= 0:
            print("La cantidad a retirar debe ser positiva.")
        else:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")

    def consultar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")
        return self.__saldo

cuenta = CuentaBanco(100)
cuenta.consultar_saldo()
cuenta.depositar(50)
cuenta.retirar(30)
cuenta.retirar(200)
cuenta.consultar_saldo()