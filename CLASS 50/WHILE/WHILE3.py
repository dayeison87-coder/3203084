class CuentaRegresiva:
    def __init__(self, inicio):
        self.inicio = inicio

    def iniciar(self):
        while self.inicio > 0:
            print(self.inicio)
            self.inicio -= 1
        print("¡Despegue!")

c = CuentaRegresiva(5)
c.iniciar()
