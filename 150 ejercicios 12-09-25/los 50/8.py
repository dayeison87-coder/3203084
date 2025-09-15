nota = 8.5
if nota >= 9:
    clasificacion = "Excelente"
elif nota >= 7:
    clasificacion = "Bueno"
    mensaje = "Sigue esforzándote"
elif nota >= 5:
    clasificacion = "Regular"
    mensaje = "Puedes mejorar"
else:
    clasificacion = "Insuficiente"
    mensaje = "Necesitas estudiar más"
print(f"Tu calificación es: {nota}")
print(f"Clasificación: {clasificacion}")
print(mensaje)
