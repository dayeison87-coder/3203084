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

print("Jugadores que NO son delanteros:")
for j in equipo:   # ciclo for
    if j.posicion != "Delantero":
        print(f"{j.nombre} - {j.posicion}")
