class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

libros = [
    Libro("Cien años de soledad", "García Márquez"),
    Libro("El coronel no tiene quien le escriba", "García Márquez"),
    Libro("Don Quijote", "Cervantes"),
    Libro("La ciudad y los perros", "Vargas Llosa")
]

autores = {}
for libro in libros:   # bucle for
    if libro.autor in autores:
        autores[libro.autor] += 1
    else:
        autores[libro.autor] = 1

for autor, cantidad in autores.items():
    print(f"{autor}: {cantidad} libros")
