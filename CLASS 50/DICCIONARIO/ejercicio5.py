class Jugador:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion

equipo = [
    Jugador("Messi", "Delantero"),
    Jugador("Casemiro", "Mediocampista"),
    Jugador("Ramos", "Defensa"),
    Jugador("Mbappé", "Delantero"),
    Jugador("Neuer", "Portero")
]

# Diccionario clave = posición, valor = lista de jugadores
posiciones = {}

for j in equipo:  # ciclo for
    if j.posicion not in posiciones:
        posiciones[j.posicion] = []
    posiciones[j.posicion].append(j.nombre)

for pos, jugadores in posiciones.items():
    print(f"{pos}: {jugadores}")
