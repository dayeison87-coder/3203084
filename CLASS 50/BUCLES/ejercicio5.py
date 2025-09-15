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

print("Defensas del equipo:")
for j in equipo:   # bucle for
    if j.posicion == "Defensa":
        print(j.nombre)
