class Usuario:
    def _init_(self, nombre):
        self.nombre = nombre
        self.playlists = []
        self.suscripcion = None


class Contenido:
    def _init_(self, titulo, duracion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero


class Playlist:
    def _init_(self, nombre):
        self.nombre = nombre
        self.items = []

    def add(self, contenido):
        self.items.append(contenido)


class Suscripcion:
    def _init_(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio


# ejemplo
u = Usuario("Sofi")
peli = Contenido("Corto", 90, "Drama")
pl = Playlist("Favoritas")
pl.add(peli)
u.playlists.append(pl)
u.suscripcion = Suscripcion("Premium", 9.99)
print(u.nombre, "→", u.suscripcion.tipo)