from datetime import datetime

class Vehiculo:
    def __init__(self, placa, capacidad):
        self.placa = placa
        self.capacidad = capacidad
        self.ruta = None

class Ruta:
    def __init__(self, nombre, hora_salida):
        self.nombre = nombre
        self.hora_salida = hora_salida
        self.pasajeros = []

    def agregar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)

class Pasajero:
    def __init__(self, nombre):
        self.nombre = nombre

# Ejemplo
bus = Vehiculo("ABC123", 40)
ruta1 = Ruta("Centro - Norte", datetime(2025, 9, 22, 8, 0))
p1 = Pasajero("Ana")
p2 = Pasajero("Luis")

ruta1.agregar_pasajero(p1)
ruta1.agregar_pasajero(p2)

print(f"Ruta: {ruta1.nombre} - Salida: {ruta1.hora_salida.strftime('%H:%M')}")
print("Pasajeros:", [p.nombre for p in ruta1.pasajeros])
