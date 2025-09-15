class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        return f"{self.nombre} está ladrando."

    def correr(self):
        return f"{self.nombre} está corriendo."

p1 = Perro("Firulais")
print(p1.ladrar())
print(p1.correr())
