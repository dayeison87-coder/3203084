class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []

    def agregar_calificacion(self, nota):
        self.calificaciones.append(nota)

    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)


est = Estudiante("melisa", 20)
est.agregar_calificacion(4.5)
est.agregar_calificacion(3.8)
est.agregar_calificacion(5.0)
print(f"Promedio de {est.nombre}: {est.calcular_promedio():.2f}")