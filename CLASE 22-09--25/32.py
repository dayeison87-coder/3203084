from datetime import datetime

class Paciente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

class Cita:
    def __init__(self, paciente, doctor, fecha, motivo):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.motivo = motivo
        paciente.historial.append(self)

# Ejemplo
d1 = Doctor("Dra. Pérez", "Pediatría")
p1 = Paciente("Juan")
c1 = Cita(p1, d1, datetime(2025, 9, 25, 10, 0), "Control general")

print(f"Cita: {p1.nombre} con {d1.nombre} ({d1.especialidad}) el {c1.fecha}")
print("Historial médico:", [(c.motivo, c.fecha) for c in p1.historial])
