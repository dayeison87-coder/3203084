class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

    def es_cuadrado(self):
        return self.ancho == self.alto


rect = Rectangulo(20, 20)
print("Área:", rect.area())
print("Perímetro:", rect.perimetro())
print("¿Es cuadrado?", "Sí" if rect.es_cuadrado() else "No")