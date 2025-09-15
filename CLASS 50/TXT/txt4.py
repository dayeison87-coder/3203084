class Coche:
    def __init__(self, marca):
        self.marca = marca

    def arrancar(self):
        return f"El coche {self.marca} ha arrancado."

    def frenar(self):
        return f"El coche {self.marca} está frenando."

c = Coche("Toyota")
print(c.arrancar())
print(c.frenar())
