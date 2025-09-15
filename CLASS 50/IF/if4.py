class Nota:
    def __init__(self, valor):
        self.valor = valor

    def resultado(self):
        if self.valor >= 3.0:
            return "Aprobado"
        else:
            return "Reprobado"

n1 = Nota(2.5)
print(n1.resultado())
