import random

class Dado:
    def __init__(self, caras=6):
        if caras < 2:
            raise ValueError("Un dado debe tener al menos 2 caras.")
        self.caras = caras
        self.estadisticas = {i: 0 for i in range(1, caras + 1)}
        
    def lanzar(self):
        resultado = random.randint(1, self.caras)
        self.estadisticas[resultado] += 1
        return resultado
    def obtener_estadisticas(self):
        return dict(self.estadisticas)
    def total_lanzamientos(self):
        return sum(self.estadisticas.values())
    def __str__(self):
        stats = self.obtener_estadisticas()
        stat_str = '\n'.join([f"Cara {cara}: {veces} vez/veces" for cara, veces in stats.items()])
        return f"Dado de {self.caras} caras\nLanzamientos totales: {self.total_lanzamientos()}\n{stat_str}"
    
d = Dado(6)
for _ in range(10):
    print(f"Lanzamiento: {d.lanzar()}")
print("\nEstadísticas:")
print(d)
