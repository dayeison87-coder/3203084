class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

estudiantes = [
    Estudiante("Ana", 4.5),
    Estudiante("Luis", 2.8),
    Estudiante("Marta", 3.2),
    Estudiante("Juan", 4.0)
]

suma = 0
for est in estudiantes:   # ciclo for
    suma += est.nota

print("Promedio de notas:", suma / len(estudiantes))
