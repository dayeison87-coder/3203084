class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

c = Calculadora()
print(c.sumar(10, 5))
print(c.restar(10, 5))
