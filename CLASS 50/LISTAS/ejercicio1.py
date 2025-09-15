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

print("Estudiantes aprobados:")
for est in estudiantes:
    if est.nota >= 3.0:
        print(f"{est.nombre} - Nota: {est.nota}")
