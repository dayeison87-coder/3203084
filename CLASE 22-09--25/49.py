import random

class Neurona:
    def _init_(self):
        self.peso = random.uniform(-1, 1)
        self.bias = 0

    def activar(self, x):
        return x * self.peso + self.bias


class Red:
    def _init_(self, n):
        self.neuronas = [Neurona() for _ in range(n)]

    def predecir(self, inputs):
        return [n.activar(x) for n, x in zip(self.neuronas, inputs)]

    def entrenar(self, lr=0.01):
        for n in self.neuronas:
            n.peso += (random.random() - 0.5) * lr


# ejemplo
red = Red(2)
print("Predicción inicial:", red.predecir([1, 2]))
red.entrenar()