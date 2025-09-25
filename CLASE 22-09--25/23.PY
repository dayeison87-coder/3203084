import random

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor} de {self.palo}"

class Baraja:
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]

    def __init__(self):
        self.cartas = [Carta(valor, palo) for palo in self.palos for valor in self.valores]

    def mezclar(self):
        random.shuffle(self.cartas)

    def repartir(self, num_cartas):
        if num_cartas > len(self.cartas):
            raise ValueError("No hay suficientes cartas en la baraja")
        cartas_repartidas = self.cartas[:num_cartas]
        self.cartas = self.cartas[num_cartas:]
        return cartas_repartidas

class Mano:
    def __init__(self, jugador):
        self.jugador = jugador
        self.cartas = []

    def agregar_cartas(self, cartas):
        self.cartas.extend(cartas)

    def mostrar(self):
        print(f"Mano de {self.jugador}:")
        for carta in self.cartas:
            print(" -", carta)

if __name__ == "__main__":
   
    baraja = Baraja()
    baraja.mezclar()

   
    mano1 = Mano("Jugador 1")
    mano2 = Mano("Jugador 2")

 
    mano1.agregar_cartas(baraja.repartir(5))
    mano2.agregar_cartas(baraja.repartir(5))

   
    mano1.mostrar()
    mano2.mostrar()
