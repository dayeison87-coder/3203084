class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

# Diccionario clave = nombre, valor = objeto Contacto
agenda = {}

while True:  # ciclo while menú
    print("\n1. Agregar contacto\n2. Ver contactos\n3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        agenda[nombre] = Contacto(nombre, telefono)
    elif opcion == "2":
        for nombre, c in agenda.items():
            print(f"{c.nombre} - {c.telefono}")
    elif opcion == "3":
        break
    else:
        print("Opción inválida")
