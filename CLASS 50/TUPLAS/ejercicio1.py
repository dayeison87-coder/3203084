class Jugador:
    def __init__(self, nombre, posicion, estadisticas):
        self.datos = (nombre, posicion, estadisticas)  
        # estadisticas = tupla (goles, asistencias, partidos)

j1 = Jugador("Messi", "Delantero", (30, 20, 40))
j2 = Jugador("Ramos", "Defensa", (8, 3, 38))

for jugador in (j1, j2):
    nombre, posicion, estadisticas = jugador.datos
    goles, asistencias, partidos = estadisticas
    print(f"{nombre} - {posicion} | Goles: {goles}, Asistencias: {asistencias}, Partidos: {partidos}")
