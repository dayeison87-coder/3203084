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

# Diccionario con autor como clave
biblioteca = {}

for libro in libros:  # ciclo for
    if libro.autor not in biblioteca:
        biblioteca[libro.autor] = []
    biblioteca[libro.autor].append(libro.titulo)

for autor, titulos in biblioteca.items():
    print(f"{autor}: {titulos}")
