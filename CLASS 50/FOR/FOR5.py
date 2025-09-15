class Fruta:
    def __init__(self, nombre, colores):
        self.nombre = nombre
        self.colores = colores

    def mostrar_colores(self):
        for c in self.colores:
            print(f"{self.nombre} puede ser de color {c}")

f = Fruta("Manzana", ["rojo", "verde", "amarillo"])
f.mostrar_colores()
