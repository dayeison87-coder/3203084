class Libro:
    def __init__(self, titulo, autor):
        self.datos = (titulo, autor)

libro1 = Libro("Cien años de soledad", "García Márquez")
libro2 = Libro("Don Quijote", "Cervantes")

for l in (libro1, libro2):
    titulo, autor = l.datos
    print(f"Título: {titulo}, Autor: {autor}")
