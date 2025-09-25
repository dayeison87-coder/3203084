from abc import ABC, abstractmethod

class Instrumento(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def tocar(self):
        pass

class Guitarra(Instrumento):
    def tocar(self):
        print(f"La {self.nombre} suena: GUITARRA rasgueando acordes")

class Piano(Instrumento):
    def tocar(self):
        print(f"El {self.nombre} suena: PIANO tocando melodías suaves")



class Bateria(Instrumento):
    def tocar(self):
        print(f"La {self.nombre} suena: BATERIA marcando el ritmo")



if __name__ == "__main__":
    instrumentos = [
        Guitarra("guitarra eléctrica"),
        Piano("piano de cola"),
        Bateria("batería acústica")
    ]

    for inst in instrumentos:
        inst.tocar()
