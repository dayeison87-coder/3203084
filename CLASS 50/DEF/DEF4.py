class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return f"El {self.marca} {self.modelo} ha arrancado."

    def detener(self):
        return f"El {self.marca} {self.modelo} se ha detenido."

v = Vehiculo("Toyota", "Corolla")
print(v.arrancar())
print(v.detener())
