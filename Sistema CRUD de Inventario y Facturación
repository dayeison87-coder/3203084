from __future__ import annotations
import os
import sys
from datetime import datetime
from typing import List, Dict

INVENTARIO_FILE = "inventario.txt"
FACTURAS_FILE = "facturas.txt"
IVA_PORCENTAJE = 0.19

def pause(msg="Presiona ENTER para continuar..."):
    input(msg)

def leer_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print(" Ingresa un número entero válido.")

def leer_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print(" Ingresa un número (puede tener decimales).")

def leer_str(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print(" Este campo no puede estar vacío.")

def dinero(v: float) -> str:
    return f"${v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def ensure_files_with_seed():
    """Crea archivos con datos de ejemplo si no existen."""
    if not os.path.exists(INVENTARIO_FILE):
        with open(INVENTARIO_FILE, "w", encoding="utf-8") as f:
            f.write("# id|nombre|precio|stock\n")
            f.write("1|Camiseta|30000|50\n")
            f.write("2|Pantalón|80000|30\n")
            f.write("3|Zapatos|150000|20\n")
    if not os.path.exists(FACTURAS_FILE):
        ejemplo = crear_bloque_factura({
            "id": 1001,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "cliente": "Juan Pérez",
            "items": [
                {"producto_id": 1, "nombre": "Camiseta", "cantidad": 2, "precio": 30000.0},
                {"producto_id": 2, "nombre": "Pantalón", "cantidad": 1, "precio": 80000.0},
            ]
        })
        with open(FACTURAS_FILE, "w", encoding="utf-8") as f:
            f.write(ejemplo)

# ----------------------------- Inventario -----------------------------
def leer_inventario() -> List[Dict]:
    productos = []
    if not os.path.exists(INVENTARIO_FILE):
        return productos
    with open(INVENTARIO_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            partes = line.split("|")
            if len(partes) != 4:
                continue  # línea dañada/ignoramos
            try:
                prod = {
                    "id": int(partes[0]),
                    "nombre": partes[1],
                    "precio": float(partes[2]),
                    "stock": int(partes[3]),
                }
                productos.append(prod)
            except ValueError:
                continue
    return productos

def escribir_inventario(productos: List[Dict]):
    with open(INVENTARIO_FILE, "w", encoding="utf-8") as f:
        f.write("# id|nombre|precio|stock\n")
        for p in sorted(productos, key=lambda x: x["id"]):
            f.write(f'{p["id"]}|{p["nombre"]}|{p["precio"]}|{p["stock"]}\n')

def obtener_siguiente_id(productos: List[Dict]) -> int:
    return (max((p["id"] for p in productos), default=0) + 1)

def inventario_add():
    productos = leer_inventario()
    print("\n=== Añadir Producto ===")
    nombre = leer_str("Nombre: ")
    precio = leer_float("Precio: ")
    stock = leer_int("Stock: ")
    nuevo = {
        "id": obtener_siguiente_id(productos),
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
    }
    productos.append(nuevo)
    escribir_inventario(productos)
    print(f" Producto agregado con ID {nuevo['id']}")

def inventario_list():
    productos = leer_inventario()
    print("\n=== Inventario ===")
    if not productos:
        print("No hay productos.")
        return
    print(f"{'ID':<5} {'Nombre':<20} {'Precio':>12} {'Stock':>8}")
    print("-"*50)
    for p in productos:
        print(f"{p['id']:<5} {p['nombre']:<20} {dinero(p['precio']):>12} {p['stock']:>8}")

def inventario_search():
    productos = leer_inventario()
    print("\n=== Buscar Producto ===")
    criterio = leer_str("Buscar por ID o nombre: ")
    encontrados = []
    if criterio.isdigit():
        pid = int(criterio)
        encontrados = [p for p in productos if p["id"] == pid]
    else:
        c = criterio.lower()
        encontrados = [p for p in productos if c in p["nombre"].lower()]
    if not encontrados:
        print(" No se encontraron coincidencias.")
        return
    for p in encontrados:
        print(f"- ID {p['id']}: {p['nombre']} | Precio {dinero(p['precio'])} | Stock {p['stock']}")

def inventario_update():
    productos = leer_inventario()
    print("\n=== Actualizar Producto ===")
    pid = leer_int("ID del producto: ")
    prods = [p for p in productos if p["id"] == pid]
    if not prods:
        print(" No existe ese ID.")
        return
    p = prods[0]
    print(f"Actualizando {p['nombre']} (Precio {dinero(p['precio'])}, Stock {p['stock']})")
    print("1) Cambiar precio")
    print("2) Cambiar stock")
    op = leer_str("Opción: ")
    if op == "1":
        p["precio"] = leer_float("Nuevo precio: ")
    elif op == "2":
        p["stock"] = leer_int("Nuevo stock: ")
    else:
        print(" Opción inválida.")
        return
    escribir_inventario(productos)
    print(" Producto actualizado.")

def inventario_delete():
    productos = leer_inventario()
    print("\n=== Eliminar Producto ===")
    pid = leer_int("ID del producto a eliminar: ")
    nuevos = [p for p in productos if p["id"] != pid]
    if len(nuevos) == len(productos):
        print("❌ No existe ese ID.")
        return
    escribir_inventario(nuevos)
    print(" Producto eliminado.")

# ----------------------------- Facturas -----------------------------
def calcular_totales(items: List[Dict]) -> Dict[str, float]:
    subtotal = sum(i["cantidad"] * i["precio"] for i in items)
    iva = round(subtotal * IVA_PORCENTAJE, 2)
    total = round(subtotal + iva, 2)
    return {"subtotal": round(subtotal, 2), "iva": iva, "total": total}

def crear_bloque_factura(factura: Dict) -> str:
    tot = calcular_totales(factura["items"])
    lineas = []
    lineas.append("=== FACTURA START ===")
    lineas.append(f"ID: {factura['id']}")
    lineas.append(f"Fecha: {factura.get('fecha', datetime.now().strftime('%Y-%m-%d %H:%M'))}")
    lineas.append(f"Cliente: {factura.get('cliente','Sin nombre')}")
    lineas.append("Items:")
    for it in factura["items"]:
        sub = it["cantidad"] * it["precio"]
        lineas.append(f"{it['producto_id']}|{it['nombre']}|{it['cantidad']}|{it['precio']}|{round(sub,2)}")
    lineas.append(f"Subtotal: {tot['subtotal']}")
    lineas.append(f"IVA(19%): {tot['iva']}")
    lineas.append(f"Total: {tot['total']}")
    lineas.append("=== FACTURA END ===\n")
    return "\n".join(lineas)

def leer_facturas() -> List[Dict]:
    facturas = []
    if not os.path.exists(FACTURAS_FILE):
        return facturas
    with open(FACTURAS_FILE, "r", encoding="utf-8") as f:
        contenido = f.read()
    bloques = contenido.split("=== FACTURA START ===")
    for b in bloques:
        b = b.strip()
        if not b:
            continue
        if "=== FACTURA END ===" not in b:
            continue
        cuerpo = b.split("=== FACTURA END ===")[0].strip()
        lineas = [x.strip() for x in cuerpo.splitlines() if x.strip()]
        # Parse header
        cab = {"id": None, "fecha": "", "cliente": "", "items": []}
        i = 0
        while i < len(lineas):
            ln = lineas[i]
            if ln.startswith("ID:"):
                cab["id"] = int(ln.split(":",1)[1].strip())
            elif ln.startswith("Fecha:"):
                cab["fecha"] = ln.split(":",1)[1].strip()
            elif ln.startswith("Cliente:"):
                cab["cliente"] = ln.split(":",1)[1].strip()
            elif ln.startswith("Items:"):
                i += 1
                # items until a line starting with "Subtotal:"
                while i < len(lineas) and not lineas[i].startswith("Subtotal:"):
                    partes = lineas[i].split("|")
                    if len(partes) >= 5:
                        try:
                            cab["items"].append({
                                "producto_id": int(partes[0]),
                                "nombre": partes[1],
                                "cantidad": int(partes[2]),
                                "precio": float(partes[3]),
                            })
                        except ValueError:
                            pass
                    i += 1
                continue  # important: don't i += 1 here again
            i += 1
        facturas.append(cab)
    return facturas

def escribir_facturas(facturas: List[Dict]):
    with open(FACTURAS_FILE, "w", encoding="utf-8") as f:
        for fac in sorted(facturas, key=lambda x: x["id"]):
            f.write(crear_bloque_factura(fac))

def facturas_list():
    facs = leer_facturas()
    print("\n=== Facturas ===")
    if not facs:
        print("No hay facturas.")
        return
    print(f"{'ID':<6} {'Fecha':<16} {'Cliente':<20} {'Total':>12}")
    print("-"*60)
    for fac in facs:
        tot = calcular_totales(fac["items"])
        print(f"{fac['id']:<6} {fac.get('fecha',''):<16} {fac.get('cliente',''):<20} {dinero(tot['total']):>12}")

def facturas_show():
    facs = leer_facturas()
    print("\n=== Mostrar Factura ===")
    fid = leer_int("ID de la factura: ")
    f = next((x for x in facs if x["id"] == fid), None)
    if not f:
        print(" No existe esa factura.")
        return
    tot = calcular_totales(f["items"])
    print(f"\nFactura #{f['id']} | {f.get('fecha','')} | Cliente: {f.get('cliente','')}")
    print(f"{'Idx':<4} {'ProdID':<7} {'Nombre':<20} {'Cant':>4} {'Precio':>10} {'Subtotal':>12}")
    print("-"*70)
    for idx, it in enumerate(f["items"], start=1):
        sub = it["cantidad"] * it["precio"]
        print(f"{idx:<4} {it['producto_id']:<7} {it['nombre']:<20} {it['cantidad']:>4} {dinero(it['precio']):>10} {dinero(sub):>12}")
    print("-"*70)
    print(f"{'Subtotal:':>52} {dinero(tot['subtotal']):>12}")
    print(f"{'IVA (19%):':>52} {dinero(tot['iva']):>12}")
    print(f"{'TOTAL:':>52} {dinero(tot['total']):>12}")

def obtener_siguiente_id_factura(facs: List[Dict]) -> int:
    return (max((f["id"] for f in facs), default=1000) + 1)

def facturas_create():
    facs = leer_facturas()
    fid = obtener_siguiente_id_factura(facs)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    cliente = leer_str("Nombre del cliente: ")
    items = []
    print("Agrega ítems (deja cantidad vacía para terminar).")
    while True:
        prod_input = input("ID de producto (o ENTER para terminar): ").strip()
        if not prod_input:
            break
        if not prod_input.isdigit():
            print("Ingresa un ID numérico.")
            continue
        pid = int(prod_input)
        inv = leer_inventario()
        p = next((x for x in inv if x["id"] == pid), None)
        if not p:
            print(" Producto no encontrado.")
            continue
        try:
            cant = leer_int("Cantidad: ")
        except KeyboardInterrupt:
            print()
            break
        if cant <= 0:
            print(" Cantidad debe ser positiva.")
            continue
        items.append({"producto_id": p["id"], "nombre": p["nombre"], "cantidad": cant, "precio": p["precio"]})
    if not items:
        print("No se agregaron ítems. Cancelado.")
        return
    nueva = {"id": fid, "fecha": fecha, "cliente": cliente, "items": items}
    facs.append(nueva)
    escribir_facturas(facs)
    print(f" Factura #{fid} creada.")

def facturas_delete():
    facs = leer_facturas()
    print("\n=== Eliminar Factura ===")
    fid = leer_int("ID de la factura a eliminar: ")
    nuevos = [x for x in facs if x["id"] != fid]
    if len(nuevos) == len(facs):
        print(" No existe ese ID.")
        return
    escribir_facturas(nuevos)
    print(" Factura eliminada.")

def facturas_edit():
    facs = leer_facturas()
    print("\n=== Editar Factura ===")
    fid = leer_int("ID de la factura a editar: ")
    f = next((x for x in facs if x["id"] == fid), None)
    if not f:
        print(" No existe esa factura.")
        return
    while True:
        print("\n1) Cambiar nombre de cliente")
        print("2) Agregar ítem")
        print("3) Quitar ítem")
        print("4) Cambiar cantidad de un ítem")
        print("5) Guardar y salir")
        print("0) Cancelar cambios")
        op = leer_str("Opción: ")
        if op == "1":
            f["cliente"] = leer_str("Nuevo cliente: ")
        elif op == "2":
            pid = leer_int("ID de producto: ")
            inv = leer_inventario()
            p = next((x for x in inv if x["id"] == pid), None)
            if not p:
                print(" Producto no encontrado.")
                continue
            cant = leer_int("Cantidad: ")
            if cant <= 0:
                print(" Cantidad debe ser positiva.")
                continue
            f["items"].append({"producto_id": p["id"], "nombre": p["nombre"], "cantidad": cant, "precio": p["precio"]})
        elif op == "3":
            if not f["items"]:
                print("No hay ítems para quitar.")
                continue
            idx = leer_int("Índice del ítem a quitar (1..n): ")
            if 1 <= idx <= len(f["items"]):
                f["items"].pop(idx-1)
            else:
                print("Índice inválido.")
        elif op == "4":
            if not f["items"]:
                print("No hay ítems para editar.")
                continue
            idx = leer_int("Índice del ítem a cambiar (1..n): ")
            if 1 <= idx <= len(f["items"]):
                nueva = leer_int("Nueva cantidad: ")
                if nueva <= 0:
                    print(" Cantidad debe ser positiva.")
                else:
                    f["items"][idx-1]["cantidad"] = nueva
            else:
                print("Índice inválido.")
        elif op == "5":
            escribir_facturas(facs)
            print(" Cambios guardados.")
            break
        elif op == "0":
            print("Cancelado, no se guardaron cambios.")
            break
        else:
            print("Opción inválida.")
        # Mostrar preview rápida
        tot = calcular_totales(f["items"])
        print(f"Subtotal {dinero(tot['subtotal'])} | IVA {dinero(tot['iva'])} | Total {dinero(tot['total'])}")

# ----------------------------- Menús -----------------------------
def menu_inventario():
    while True:
        print("\n=== Gestión de Inventario ===")
        print("1) Añadir producto")
        print("2) Listar productos")
        print("3) Buscar producto")
        print("4) Actualizar precio/stock")
        print("5) Eliminar producto")
        print("0) Volver")
        op = leer_str("Opción: ")
        if op == "1":
            inventario_add()
        elif op == "2":
            inventario_list()
        elif op == "3":
            inventario_search()
        elif op == "4":
            inventario_update()
        elif op == "5":
            inventario_delete()
        elif op == "0":
            return
        else:
            print(" Opción inválida.")
        pause()

def menu_facturas():
    while True:
        print("\n=== Sistema de Facturación ===")
        print("1) Crear factura")
        print("2) Listar facturas")
        print("3) Mostrar factura")
        print("4) Editar factura")
        print("5) Eliminar factura")
        print("0) Volver")
        op = leer_str("Opción: ")
        if op == "1":
            facturas_create()
        elif op == "2":
            facturas_list()
        elif op == "3":
            facturas_show()
        elif op == "4":
            facturas_edit()
        elif op == "5":
            facturas_delete()
        elif op == "0":
            return
        else:
            print(" Opción inválida.")
        pause()

def main():
    ensure_files_with_seed()
    while True:
        print("\n===============================")
        print(" Inventario & Facturación TXT ")
        print("===============================")
        print("1) Gestión de Inventario")
        print("2) Sistema de Facturación")
        print("0) Salir")
        op = leer_str("Opción: ")
        if op == "1":
            menu_inventario()
        elif op == "2":
            menu_facturas()
        elif op == "0":
            print("¡Hasta pronto!")
            break
        else:
            print(" Opción inválida.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario.")
