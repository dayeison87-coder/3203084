from datetime import datetime, timedelta

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prestamos = []

class Prestamo:
    def __init__(self, libro, usuario, dias=7):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_vencimiento = self.fecha_prestamo + timedelta(days=dias)
        libro.disponible = False
        usuario.prestamos.append(self)

    def multa(self):
        if datetime.now() > self.fecha_vencimiento:
            dias_retraso = (datetime.now() - self.fecha_vencimiento).days
            return dias_retraso * 2  # $2 por día
        return 0

# Ejemplo
l1 = Libro("1984", "George Orwell")
u1 = Usuario("Pedro")
prestamo = Prestamo(l1, u1, 3)

print("Libro prestado a:", u1.nombre)
print("Multa:", prestamo.multa())
