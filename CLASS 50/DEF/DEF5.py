class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def estado(self):
        if self.promedio() >= 3.0:
            return "Aprobado"
        else:
            return "Reprobado"

e = Estudiante("Carlos", [4.0, 2.5, 3.5])
print(e.promedio())
print(e.estado())
