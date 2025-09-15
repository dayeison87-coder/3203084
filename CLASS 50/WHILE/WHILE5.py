class Bateria:
    def __init__(self, carga):
        self.carga = carga

    def usar(self):
        while self.carga > 0:
            print(f"Batería al {self.carga}%")
            self.carga -= 10
        print("¡Batería agotada!")

b = Bateria(50)
b.usar()


