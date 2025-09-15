class TablaMultiplicar:
    def __init__(self, numero):
        self.numero = numero

    def mostrar_tabla(self):
        for i in range(1, 11):
            print(f"{self.numero} x {i} = {self.numero * i}")

t = TablaMultiplicar(5)
t.mostrar_tabla()
