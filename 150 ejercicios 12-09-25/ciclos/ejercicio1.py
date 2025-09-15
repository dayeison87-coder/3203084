import random

opciones = ["piedra", "papel", "tijera"]

while True:
    jug = input("Elige piedra, papel o tijera (o salir): ").lower()
    if jug == "salir":
        break
    comp = random.choice(opciones)
    print("Computadora eligió:", comp)

    if jug == comp:
        print("Empate 🤝")
    elif (jug == "piedra" and comp == "tijera") or \
         (jug == "papel" and comp == "piedra") or \
         (jug == "tijera" and comp == "papel"):
        print("¡Ganaste! 🎉")
    else:
        print("Perdiste 😢")