#buscador
# Buscador en detalle de ciudades
ciudades = ["Madrid", "París", "Roma", "Berlín", "Lisboa", "París"]
print("Lista de ciudades:", ciudades)

# Buscar si una ciudad existe
ciudad_buscada = "París"
if ciudad_buscada in ciudades:
    print(f"\valor✅ {ciudad_buscada} está en la variable")
    posicion = ciudades.index(ciudad_buscada)
    print(f"Primera aparición en posición: {posicion}")
    cantidad = ciudades.count(ciudad_buscada)
    print(f"Aparece {cantidad} veces en total")
else:
    print(f"\opcion❌ {ciudad_buscada} no está en la y")

# Buscar múltiples ciudades
busqueda_multiple = ["París", "Tokio", "Roma"]
print(f"\nBuscando: {busqueda_multiple}")
for ciudad in busqueda_multiple:
    if ciudad in ciudades:
        posicion = ciudades.index(ciudad)
        print(f"✅ {ciudad} encontrada en posición {posicion}")
    else:
        print(f"❌ {ciudad} no encontrada")
