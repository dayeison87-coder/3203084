import time

class Semaforo:
    def __init__(self, tiempo_rojo=5, tiempo_amarillo=2, tiempo_verde=5):
        self.estados = ['rojo', 'verde', 'amarillo']
        self.tiempos = {
            'rojo': tiempo_rojo,
            'amarillo': tiempo_amarillo,
            'verde': tiempo_verde
        }
        self.estado_actual = 'rojo'

    def cambiar_estado(self):
        idx = self.estados.index(self.estado_actual)
        self.estado_actual = self.estados[(idx + 1) % len(self.estados)]
        print(f" Cambio a estado: {self.estado_actual.upper()} (duración: {self.tiempos[self.estado_actual]}s)")

    def iniciar(self, ciclos=3):
        for _ in range(ciclos * len(self.estados)):
            print(f"Estado actual: {self.estado_actual.upper()}")
            time.sleep(self.tiempos[self.estado_actual])
            self.cambiar_estado()

semaforo = Semaforo(tiempo_rojo=3, tiempo_amarillo=1, tiempo_verde=3)
semaforo.iniciar(ciclos=2)
