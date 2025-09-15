class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor(self):
        if self.edad >= 18:
            return f"{self.nombre} es mayor de edad."
        else:
            return f"{self.nombre} es menor de edad."

p1 = Persona("Ana", 20)
print(p1.es_mayor())