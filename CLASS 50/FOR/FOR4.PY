class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def promedio(self):
        suma = 0
        for n in self.notas:
            suma += n
        return suma / len(self.notas)

e = Estudiante("Laura", [4.0, 3.5, 5.0])
print(f"Promedio de {e.nombre}: {e.promedio():.2f}")
