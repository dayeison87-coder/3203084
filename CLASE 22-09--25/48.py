class Animal:
    def _init_(self, nombre, energia=10):
        self.nombre = nombre
        self.energia = energia

    def comer(self, obj):
        self.energia += getattr(obj, "energia", 1)

    def andar(self):
        self.energia -= 1


class Planta:
    def _init_(self, nombre, energia=2):
        self.nombre = nombre
        self.energia = energia


class Ambiente:
    def _init_(self):
        self.seres = []

    def agregar(self, ser):
        self.seres.append(ser)


class Cadena:
    def _init_(self):
        self.eslabones = []


# ejemplo
conejo = Animal("Conejo")
hierba = Planta("Hierba")
conejo.comer(hierba)
print(conejo.nombre, "Energía:", conejo.energia)