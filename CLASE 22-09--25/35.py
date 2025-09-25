class Candidato:
    def __init__(self, nombre, partido):
        self.nombre = nombre
        self.partido = partido
        self.votos = 0

    def recibir_voto(self):
        self.votos += 1

class Votante:
    def __init__(self, nombre, id_votante):
        self.nombre = nombre
        self.id_votante = id_votante
        self.voto_realizado = False

    def votar(self, candidato):
        if not self.voto_realizado:
            candidato.recibir_voto()
            self.voto_realizado = True
            print(f"{self.nombre} ha votado por {candidato.nombre}")
        else:
            print(f"{self.nombre} ya votó")

class Eleccion:
    def __init__(self):
        self.candidatos = []

    def agregar_candidato(self, candidato):
        self.candidatos.append(candidato)

    def resultados(self):
        for c in self.candidatos:
            print(f"{c.nombre} ({c.partido}): {c.votos} votos")

# Ejemplo
c1 = Candidato("Ana", "Partido A")
c2 = Candidato("Luis", "Partido B")
eleccion = Eleccion()
eleccion.agregar_candidato(c1)
eleccion.agregar_candidato(c2)

v1 = Votante("Pedro", "123")
v2 = Votante("Lucía", "456")

v1.votar(c1)
v2.votar(c2)
v2.votar(c1)  # Intento de votar dos veces

eleccion.resultados()
