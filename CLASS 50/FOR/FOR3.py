class Palabra:
    def __init__(self, texto):
        self.texto = texto

    def contar_vocales(self):
        vocales = "aeiouAEIOU"
        contador = 0
        for letra in self.texto:
            if letra in vocales:
                contador += 1
        return contador

p = Palabra("Programación")
print("Número de vocales:", p.contar_vocales())
