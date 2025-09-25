class Avatar:
    def _init_(self, nombre):
        self.nombre = nombre
        self.pos = {"x": 0, "y": 0}
        self.inventario = []

    def mover(self, dx, dy):
        self.pos["x"] += dx
        self.pos["y"] += dy

    def recoger(self, obj):
        self.inventario.append(obj)


class Mundo:
    def _init_(self, nombre):
        self.nombre = nombre
        self.objetos = []

    def add(self, obj):
        self.objetos.append(obj)


class Objeto:
    def _init_(self, nombre):
        self.nombre = nombre

    def interactuar(self, avatar):
        avatar.recoger(self)


# ejemplo
ava = Avatar("Ava")
mundo = Mundo("Servidor1")
moneda = Objeto("Moneda")
mundo.add(moneda)
moneda.interactuar(ava)
print(ava.nombre, "Inventario:", [o.nombre for o in ava.inventario])