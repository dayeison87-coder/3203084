class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

    def cumpleaños(self):
        self.edad += 1
        return f"Feliz cumpleaños {self.nombre}, ahora tienes {self.edad} años."

p = Persona("Ana", 20)
print(p.presentarse())
print(p.cumpleaños())
