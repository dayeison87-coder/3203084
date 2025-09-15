class Vehiculo:
    def __init__(self, combustible):
        self.combustible = combustible

    def arrancar(self):
        if self.combustible > 0:
            return "El vehículo ha arrancado."
        else:
            return "No hay combustible."

carro = Vehiculo(0)
print(carro.arrancar())
