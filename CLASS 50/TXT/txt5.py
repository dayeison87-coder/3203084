class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def mostrar(self):
        return f"Estudiante: {self.nombre}, Promedio: {self.promedio():.2f}"

e = Estudiante("María", [4.5, 3.8, 5.0])
print(e.mostrar())
