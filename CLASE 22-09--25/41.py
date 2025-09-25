class Cuenta:
    def _init_(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.movimientos = []

    def depositar(self, monto):
        self.saldo += monto
        self.movimientos.append(("depósito", monto))

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            self.movimientos.append(("retiro", monto))
            return True
        return False


class Transaccion:
    def _init_(self, origen, destino, monto):
        self.origen = origen
        self.destino = destino
        self.monto = monto


class Tarjeta:
    def _init_(self, numero, cuenta):
        self.numero = numero
        self.cuenta = cuenta
        self.activa = True

    def bloquear(self):
        self.activa = False


class Prestamo:
    def _init_(self, monto, interes_anual, cuotas):
        self.monto = monto
        self.interes_anual = interes_anual
        self.cuotas = cuotas

    def pago_mensual(self):
        r = self.interes_anual / 12
        return (self.monto * r) / (1 - (1 + r) ** -self.cuotas)


# ejemplo
c = Cuenta("Ana", 500)
c.depositar(200)
c.retirar(100)
p = Prestamo(1000, 0.12, 12)
print("Saldo:", c.saldo, "Pago mensual:", round(p.pago_mensual(), 2))