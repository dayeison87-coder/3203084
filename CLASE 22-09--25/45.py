class Paciente:
    def _init_(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.historial = []

    def agregar_tratamiento(self, trat):
        self.historial.append(trat)


class Doctor:
    def _init_(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad


class Departamento:
    def _init_(self, nombre):
        self.nombre = nombre
        self.doctores = []

    def add_doctor(self, doc):
        self.doctores.append(doc)


class Tratamiento:
    def _init_(self, descripcion):
        self.descripcion = descripcion


# ejemplo
p = Paciente("Diego", "P001")
t = Tratamiento("Observación")
p.agregar_tratamiento(t)
print(p.nombre, "Historial:", [tr.descripcion for tr in p.historial])