import random

class Personaje:
    def __init__(self, nombre, vida=100, fuerza=10):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.experiencia = 0
        self.inventario = []

    def atacar(self, enemigo):
        dano = random.randint(1, self.fuerza)
        enemigo.vida -= dano
        print(f"{self.nombre} ataca a {enemigo.nombre} y causa {dano} de daño")

        if enemigo.vida <= 0:
            print(f"{enemigo.nombre} ha sido derrotado")
            self.experiencia += 10

    def usar_item(self, item):
        item.usar(self)

class Habilidad:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

class Item:
    def __init__(self, nombre, efecto):
        self.nombre = nombre
        self.efecto = efecto

    def usar(self, personaje):
        personaje.vida += self.efecto
        print(f"{personaje.nombre} usa {self.nombre} y recupera {self.efecto} de vida")

# Ejemplo
p1 = Personaje("Guerrero")
p2 = Personaje("Orco", vida=50, fuerza=8)

p1.atacar(p2)
p2.atacar(p1)

pocion = Item("Poción de vida", 20)
p1.usar_item(pocion)
