class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya está disponible.")

    def mostrar_estado(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}")

libro = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728")
libro.mostrar_estado()
libro.prestar()
libro.mostrar_estado()
libro.devolver()
libro.mostrar_estado()