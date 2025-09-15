class ListaNumeros:
    def __init__(self, numeros):
        self.numeros = numeros

    def mostrar(self):
        for n in self.numeros:
            print(n)

l = ListaNumeros([10, 20, 30, 40])
l.mostrar()
