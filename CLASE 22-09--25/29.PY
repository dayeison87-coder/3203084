from datetime import datetime

class Recurso:
    def __init__(self, nombre):
        self.nombre = nombre

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Reserva:
    def __init__(self, recurso, usuario, fecha):
        self.recurso = recurso
        self.usuario = usuario
        self.fecha = fecha

# Ejemplo
sala = Recurso("Sala de reuniones")
u1 = Usuario("Laura")
res = Reserva(sala, u1, datetime(2025, 9, 23, 10, 0))

print(f"{u1.nombre} reservó {sala.nombre} para el {res.fecha}")
