# 20. Contar cuántas veces aparece una letra en un texto
print("Contar ocurrencias de una letra en un texto:")
texto = input("Ingrese un texto: ")
letra = input("Ingrese la letra a buscar: ")
i = 0
contador = 0
while i < len(texto):
    if texto[i] == letra:
        contador += 1
    i += 1
print(f"La letra '{letra}' aparece {contador} veces en el texto.\n")