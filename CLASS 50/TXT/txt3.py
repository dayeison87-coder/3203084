class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar(self):
        return f"'{self.titulo}' escrito por {self.autor}"

l = Libro("Cien años de soledad", "Gabriel García Márquez")
print(l.mostrar())
