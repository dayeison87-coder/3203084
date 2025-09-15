class SumaNumeros:
    def __init__(self, limite):
        self.limite = limite

    def sumar(self):
        total = 0
        num = 1
        while total + num <= self.limite:
            total += num
            num += 1
        return total

s = SumaNumeros(20)
print("Suma total:", s.sumar())
