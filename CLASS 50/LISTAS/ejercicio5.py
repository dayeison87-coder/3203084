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

print("Equipo completo:")
for j in equipo:
    print(f"{j.nombre} - {j.posicion}")

print("\nDelanteros del equipo:")
delanteros = [j.nombre for j in equipo if j.posicion == "Delantero"]
for d in delanteros:
    print(d)
