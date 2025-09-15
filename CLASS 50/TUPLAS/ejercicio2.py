class Contacto:
    def __init__(self, nombre, telefono):
        self.datos = (nombre, telefono)

c1 = Contacto("Pedro", "12345")
c2 = Contacto("Ana", "67890")

for contacto in (c1, c2):  # tupla de objetos
    nombre, telefono = contacto.datos
    print(f"Nombre: {nombre} - Teléfono: {telefono}")
