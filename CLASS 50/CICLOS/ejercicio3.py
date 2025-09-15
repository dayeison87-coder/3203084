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

autores = []
for libro in libros:   # ciclo for externo
    if libro.autor not in autores:
        autores.append(libro.autor)

for autor in autores:  # ciclo for interno
    contador = 0
    for libro in libros:
        if libro.autor == autor:
            contador += 1
    print(f"{autor}: {contador} libros")
