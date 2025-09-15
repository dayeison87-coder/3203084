class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono


agenda = []

def agregar_contacto(nombre, telefono):
    agenda.append(Contacto(nombre, telefono))

def buscar_contacto(nombre):
    for c in agenda:
        if c.nombre == nombre:
            return f"{c.nombre} - {c.telefono}"
    return "Contacto no encontrado"

def eliminar_contacto(nombre):
    global agenda
    agenda = [c for c in agenda if c.nombre != nombre]

agregar_contacto("Pedro", "12345")
agregar_contacto("Ana", "67890")
agregar_contacto("Luis", "54321")

print(buscar_contacto("Ana"))
eliminar_contacto("Pedro")

print("\nAgenda actual:")
for c in agenda:
    print(f"{c.nombre} - {c.telefono}")
