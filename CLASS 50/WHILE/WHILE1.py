class Contador:
    def __init__(self, limite):
        self.limite = limite

    def contar(self):
        i = 1
        while i <= self.limite:
            print(i)
            i += 1

c = Contador(5)
c.contar()
