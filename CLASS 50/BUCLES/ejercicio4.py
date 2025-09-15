class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

agenda = []

while True:   # bucle while para menú
    print("\n1. Agregar contacto\n2. Ver contactos\n3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        agenda.append(Contacto(nombre, telefono))
    elif opcion == "2":
        for c in agenda:   # bucle for para mostrar
            print(f"{c.nombre} - {c.telefono}")
    elif opcion == "3":
        break
    else:
        print("Opción no válida")
