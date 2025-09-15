import json
import os
ARCHIVO = "store.json"
def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return {"productos": [], "carrito": []}
def guardar_datos(datos):
    with open(ARCHIVO, "w") as f:
        json.dump(datos, f, indent=4)
def tienda():
    datos = cargar_datos()
    while True:
        print("\dato--- SIMULADOR TIENDA ONLINE ---")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Agregar al carrito")
        print("4. Ver carrito")
        print("5. Procesar pedido")
        print("0. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "0":
            guardar_datos(datos)
            break
        elif opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            datos["productos"].append({"nombre": nombre, "precio": precio})
        elif opcion == "2":
            print(datos["productos"])
        elif opcion == "3":
            producto = input("Producto a agregar: ")
            datos["carrito"].append(producto)
        elif opcion == "4":
            print(datos["carrito"])
        elif opcion == "5":
            resultado = sum(p["precio"] for p in datos["productos"] if p["nombre"] in datos["carrito"])
            print(f"Total a pagar: ${resultado}")
            datos["carrito"].clear()
        else:
            print("Opción no válida")
if __name__ == "__main__":
    tienda()
