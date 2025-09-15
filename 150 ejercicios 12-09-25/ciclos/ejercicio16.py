colores = {}
for i in range(5):
    color = input(f"Persona {i+1}, ¿color favorito?: ").lower()
    if color in colores:
        colores[color] += 1
    else:
        colores[color] = 1
print("Resultados de la encuesta:", colores)