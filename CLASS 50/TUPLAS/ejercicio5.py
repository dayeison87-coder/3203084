class Estudiante:
    def __init__(self, nombre, notas):
        self.datos = (nombre, notas) 

est1 = Estudiante("Ana", (4.5, 3.8, 4.2))
est2 = Estudiante("Luis", (2.8, 3.0, 3.5))

for est in (est1, est2): 
    nombre, notas = est.datos
    promedio = sum(notas) / len(notas)
    print(f"{nombre} - Notas: {notas} - Promedio: {promedio}")
