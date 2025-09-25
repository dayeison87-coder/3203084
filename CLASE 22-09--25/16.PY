class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def describir(self):
        return f"{self.color} {self.marca} {self.modelo}"

    def encender(self):
        return "Vehículo encendido."

    def apagar(self):
        return "Vehículo apagado."
    
class Carro(Vehiculo):
    def __init__(self, marca, modelo, color, puertas, tipo_combustible):
        super().__init__(marca, modelo, color)
        self.puertas = puertas
        self.tipo_combustible = tipo_combustible

    def tocar_claxon(self):
        return "¡Beep beep!"

    def describir(self):
        return f"{super().describir()} - {self.puertas} puertas, Combustible: {self.tipo_combustible}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, color, cilindrada, tipo):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada
        self.tipo = tipo

    def hacer_caballito(self):
        return "¡Haciendo un caballito!"

    def describir(self):
        return f"{super().describir()} - {self.cilindrada}cc, Tipo: {self.tipo}"
    
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color, tipo, tiene_cambios):
        super().__init__(marca, modelo, color)
        self.tipo = tipo  # Ejemplo: montaña, ruta, urbana
        self.tiene_cambios = tiene_cambios

    def pedalear(self):
        return "Pedaleando..."

    def describir(self):
        cambios = "con cambios" if self.tiene_cambios else "sin cambios"
        return f"{super().describir()} - Tipo: {self.tipo}, {cambios}"
    
carro = Carro("Honda", "Civic", "Gris", 4, "Gasolina")
print(carro.describir())
print(carro.tocar_claxon())

moto = Motocicleta("Kawasaki", "Ninja", "Verde", 650, "Deportiva")
print(moto.describir())
print(moto.hacer_caballito())

bici = Bicicleta("Giant", "Escape 3", "Azul", "Urbana", True)
print(bici.describir())
print(bici.pedalear())



    
