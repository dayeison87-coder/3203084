numero_secreto= 7
adivinanza= 5
print(f"Número secreto: {numero_secreto}")
print(f"Tu adivinanza: {adivinanza}")
if adivinanza == numero_secreto:
    print("¡Felicidades! Has adivinado el número secreto.")
elif adivinanza < numero_secreto:
    print("Tu adivinanza es muy baja. Intenta de nuevo.")
else:
    print("Tu adivinanza es muy alta. Intenta de nuevo.")
