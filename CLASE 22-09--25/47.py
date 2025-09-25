class Paquete:
    def _init_(self, id, peso, destino):
        self.id = id
        self.peso = peso
        self.destino = destino
        self.estado = "almacén"


class Vehiculo:
    def _init_(self, id, capacidad):
        self.id = id
        self.capacidad = capacidad
        self.carga = []

    def cargar(self, paquete):
        if sum(p.peso for p in self.carga) + paquete.peso <= self.capacidad:
            self.carga.append(paquete)
            paquete.estado = "en ruta"
            return True
        return False


class Ruta:
    def _init_(self, origen, destino, distancia):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia


class Almacen:
    def _init_(self):
        self.paquetes = []

    def recibir(self, paquete):
        self.paquetes.append(paquete)


# ejemplo
paq = Paquete("PK1", 5, "Cali")
veh = Vehiculo("V1", 10)
print("Se cargó?", veh.cargar(paq))