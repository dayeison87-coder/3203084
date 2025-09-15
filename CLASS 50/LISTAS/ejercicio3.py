class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
libros = [
    Libro("Cien años de soledad", "Gabriel García Márquez"),
    Libro("El coronel no tiene quien le escriba", "Gabriel García Márquez"),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes"),
    Libro("La ciudad y los perros", "Mario Vargas Llosa")
]

def buscar_por_autor(lista, autor):
    return [libro.titulo for libro in lista if libro.autor == autor]

autor_buscar = "Gabriel García Márquez"
resultados = buscar_por_autor(libros, autor_buscar)

print(f"Libros de {autor_buscar}:")
for titulo in resultados:
    print(titulo)
