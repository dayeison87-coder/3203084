class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.seguidos = []
        self.publicaciones = []

    def seguir(self, otro):
        if otro not in self.seguidos:
            self.seguidos.append(otro)

    def publicar(self, texto):
        pub = Publicacion(self, texto)
        self.publicaciones.append(pub)
        return pub

class Publicacion:
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto
        self.likes = 0
        self.comentarios = []

    def dar_like(self):
        self.likes += 1

    def comentar(self, usuario, texto):
        self.comentarios.append(Comentario(usuario, texto))

class Comentario:
    def __init__(self, usuario, texto):
        self.usuario = usuario
        self.texto = texto

# Ejemplo
u1 = Usuario("Carlos")
u2 = Usuario("Luisa")

u1.seguir(u2)
pub = u2.publicar("Hola, mundo!")
pub.dar_like()
pub.comentar(u1, "¡Buen post!")

print(f"{pub.autor.nombre} publicó: {pub.texto} ({pub.likes} likes)")
for c in pub.comentarios:
    print(f"- {c.usuario.nombre}: {c.texto}")
