class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono):
        contacto = Contacto(nombre, telefono)
        self.contactos.append(contacto)
        print(f"Contacto agregado: {nombre}")

    def buscar_contacto(self, nombre):
        encontrados = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]
        if encontrados:
            for c in encontrados:
                print(f"Nombre: {c.nombre}, Teléfono: {c.telefono}")
        else:
            print("Contacto no encontrado.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            for c in self.contactos:
                print(f"Nombre: {c.nombre}, Teléfono: {c.telefono}")


agenda = Agenda()
agenda.agregar_contacto("Ana", "23515")
agenda.agregar_contacto("Luis", "45131")
agenda.mostrar_contactos()
agenda.buscar_contacto("Ana")
agenda.buscar_contacto("Pedro")