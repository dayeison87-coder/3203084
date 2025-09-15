class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

agenda = []

opcion = ""
while opcion != "3":   # ciclo while menú
    print("\n1. Agregar contacto\n2. Ver contactos\n3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        agenda.append(Contacto(nombre, telefono))
    elif opcion == "2":
        for c in agenda:   # ciclo for
            print(f"{c.nombre} - {c.telefono}")
    elif opcion == "3":
        print("Saliendo...")
    else:
        print("Opción no válida")
