import math

class Forma:
    def area(self):
        raise NotImplementedError("Debe implementar el método area.")

    def perimetro(self):
        raise NotImplementedError("Debe implementar el método perimetro.")

class Poligono(Forma):
    def __init__(self, lados):
        self.lados = lados 


class Triangulo(Poligono):
    def __init__(self, lado1, lado2, lado3):
        super().__init__([lado1, lado2, lado3])

    def perimetro(self):
        return sum(self.lados)

    def area(self):
        s = self.perimetro() / 2
        a, b, c = self.lados
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cuadrado(Poligono):
    def __init__(self, lado):
        super().__init__([lado] * 4)
        self.lado = lado

    def perimetro(self):
        return 4 * self.lado

    def area(self):
        return self.lado ** 2

class Pentagono(Poligono):
    def __init__(self, lado):
        super().__init__([lado] * 5)
        self.lado = lado

    def perimetro(self):
        return 5 * self.lado

    def area(self):
        return (5 * self.lado**2) / (4 * math.tan(math.pi / 5))

if __name__ == "__main__":
    t = Triangulo(3, 4, 5)
    print("Triángulo - Área:", round(t.area(), 2), "Perímetro:", t.perimetro())

    c = Cuadrado(6)
    print("Cuadrado - Área:", c.area(), "Perímetro:", c.perimetro())

    p = Pentagono(5)
    print("Pentágono - Área:", round(p.area(), 2), "Perímetro:", p.perimetro())
