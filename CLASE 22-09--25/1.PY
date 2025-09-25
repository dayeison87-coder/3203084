class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, soy un(a) {self.especie} y tengo {self.edad} años.")


mascota1 = Mascota("Luna", "gato", 2)
mascota2 = Mascota("Rex", "perro", 5)
mascota3 = Mascota("Kiwi", "loro", 1)

mascota1.presentarse()
mascota2.presentarse()
mascota3.presentarse()