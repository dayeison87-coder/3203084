import random

class JuegoAdivinar:
    def __init__(self):
        self.numero = random.randint(1, 10)

    def jugar(self):
        intento = 0
        adivinado = False
        while not adivinado:
            intento += 1
            valor = int(input("Adivina el número (1-10): "))
            if valor == self.numero:
                print(f"¡Correcto! Lo lograste en {intento} intentos.")
                adivinado = True

