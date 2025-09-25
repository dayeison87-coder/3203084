import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def circunferencia(self):
        return 2 * math.pi * self.radio

    def comparar(self, otro):
        if self.radio > otro.radio:
            return "Este círculo es más grande."
        elif self.radio < otro.radio:
            return "El otro círculo es más grande."
        else:
            return "Ambos círculos son iguales."

c1 = Circulo(5)
c2 = Circulo(7)
print("Área c1:", c1.area())
print("Circunferencia c1:", c1.circunferencia())
print(c1.comparar(c2))