class Freelancer:
    def _init_(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def calificar(self, n):
        self.calificaciones.append(n)

    def promedio(self):
        return sum(self.calificaciones)/len(self.calificaciones) if self.calificaciones else 0


class Cliente:
    def _init_(self, nombre):
        self.nombre = nombre


class Proyecto:
    def _init_(self, titulo, presupuesto):
        self.titulo = titulo
        self.presupuesto = presupuesto
        self.propuestas = []

    def recibir(self, propuesta):
        self.propuestas.append(propuesta)


class Propuesta:
    def _init_(self, freelancer, monto, mensaje):
        self.freelancer = freelancer
        self.monto = monto
        self.mensaje = mensaje


# ejemplo
f = Freelancer("Luis")
p = Proyecto("Web", 500)
p.recibir(Propuesta(f, 450, "Lo hago rápido"))
print(p.titulo, "Propuestas:", len(p.propuestas))