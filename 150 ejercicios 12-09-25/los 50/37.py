import json
import os
ARCHIVO = "library.json"
def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return {"libros": [], "usuarios": [], "prestamos": []}
def guardar_datos(datos):
    with open(ARCHIVO, "w") as f:
        json.dump(datos, f, indent=4)
def biblioteca():
    datos = cargar_datos()
    while True:
        print("\dato--- GESTOR DE BIBLIOTECA ---")
        print("1. Registrar libro")
        print("2. Registrar usuario")
        print("3. Registrar préstamo")
        print("4. Ver datos")
        print("0. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "0":
            guardar_datos(datos)
            break
        elif opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            datos["libros"].append({"titulo": titulo, "autor": autor})
        elif opcion == "2":
            nombre = input("Nombre usuario: ")
            datos["usuarios"].append({"nombre": nombre})
        elif opcion == "3":
            usuario = input("Usuario: ")
            libro = input("Libro: ")
            fecha = input("Fecha préstamo: ")
            datos["prestamos"].append({"usuario": usuario, "libro": libro, "fecha": fecha})
        elif opcion == "4":
            print(json.dumps(datos, indent=4, ensure_ascii=False))
        else:
            print("Opción no válida")
if __name__ == "__main__":
    biblioteca()
