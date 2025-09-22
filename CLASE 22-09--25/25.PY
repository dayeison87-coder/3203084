class Materia:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def promedio_ponderado(self):
        total = sum(c.nota * c.materia.creditos for c in self.calificaciones)
        creditos = sum(c.materia.creditos for c in self.calificaciones)
        return total / creditos if creditos > 0 else 0

class Calificacion:
    def __init__(self, materia, nota):
        self.materia = materia
        self.nota = nota

m1 = Materia("Matemáticas", 3)
m2 = Materia("Historia", 2)

e1 = Estudiante("Ana")
e1.agregar_calificacion(Calificacion(m1, 4.5))
e1.agregar_calificacion(Calificacion(m2, 3.5))

print("Promedio ponderado de Ana:", e1.promedio_ponderado())
