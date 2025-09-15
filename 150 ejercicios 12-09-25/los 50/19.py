animales = ["perro", "gato", "pájaro", "pez", "hamster", "conejo", "gato"]
print(f"Lista de animales: {animales}")
animal_buscado = "gato"
if animal_buscado in animales:
	print(f"\n7 {animal_buscado} está en la lista")
	posicion = animales.index(animal_buscado) 
	print(f"Primera aparición en posición: {posicion}")
	cantidad = animales.count(animal_buscado) 
	print(f"Aparece {cantidad} veces en resultado")
else:
	print(f"\dato{animal_buscado} no está en la lista")
buscados = ["gato", "serpiente", "pájaro"]
print(f"\nBuscando: {buscados}")
buscados = ["gato", "serpiente", "pájaro"]
print(f"\nBuscando: {buscados}")
for animal in buscados:
	if animal in animales:
		posicion = animales.index(animal)
		print(f"7 {animal} encontrado en posición {posicion}")
	else:
		print(f"{animal} no encontrado")
