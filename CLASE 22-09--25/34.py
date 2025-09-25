class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clases = []

class Profesor:
    def __init__(self, nombre, instrumento):
        self.nombre = nombre
        self.instrumento = instrumento

class Clase:
    def __init__(self, estudiante, profesor, horario):
        self.estudiante = estudiante
        self.profesor = profesor
        self.horario = horario
        self.progreso = 0
        estudiante.clases.append(self)

    def avanzar(self, puntos):
        self.progreso += puntos
        if self.progreso > 100:
            self.progreso = 100

# Ejemplo
e1 = Estudiante("María")
p1 = Profesor("Carlos", "Piano")
clase1 = Clase(e1, p1, "Lunes 10:00 AM")
clase1.avanzar(30)

print(f"{e1.nombre} tiene clase de {p1.instrumento} con {p1.nombre}")
print(f"Progreso: {clase1.progreso}%")
