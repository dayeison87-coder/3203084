class Reloj:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas % 24
        self.minutos = minutos % 60
        self.segundos = segundos % 60

    def avanzar(self, segundos):
        self.segundos += segundos
        self.minutos += self.segundos // 60
        self.segundos = self.segundos % 60
        self.horas += self.minutos // 60
        self.minutos = self.minutos % 60
        self.horas = self.horas % 24

    def mostrar(self):
        print(f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}")


reloj = Reloj(23, 59, 50)
reloj.mostrar()
reloj.avanzar(15)
reloj.mostrar()