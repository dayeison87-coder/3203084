# 16. Juego de adivinar un número secreto
print("Juego: adivina el número secreto (entre 1 y 10)")
secreto = 7
intento = 0
while intento != secreto:
    intento = int(input("Adivina el número: "))
    if intento < secreto:
        print("El número es mayor.")
    elif intento > secreto:
        print("El número es menor.")
print("¡Correcto! Has adivinado el número.\n")