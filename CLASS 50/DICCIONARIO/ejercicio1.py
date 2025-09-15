class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

# Diccionario con clave = nombre, valor = objeto Estudiante
estudiantes = {
    "Ana": Estudiante("Ana", 4.5),
    "Luis": Estudiante("Luis", 2.8),
    "Marta": Estudiante("Marta", 3.2)
}

for nombre, obj in estudiantes.items():  # ciclo for sobre diccionario
    print(f"{nombre} - Nota: {obj.nota}")
