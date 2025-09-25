from datetime import datetime, timedelta

class Empleado:
    def __init__(self, nombre, rol=None):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.rol = rol

class Tarea:
    def __init__(self, titulo, duracion_dias=1):
        self.id = str(uuid.uuid4())
        self.titulo = titulo
        self.duracion = int(duracion_dias)
        self.asignado = None
        self.estado = "PENDIENTE"
        self.dependencias = set()  
        self.inicio_estimado = None
        self.fin_estimado = None

    def agregar_dependencia(self, tarea):
        self.dependencias.add(tarea.id)

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []

    def agregar_miembro(self, empleado):
        self.miembros.append(empleado)

class Proyecto:
    def __init__(self, nombre, fecha_inicio: datetime):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.tareas = {}

    def agregar_tarea(self, tarea: Tarea):
        self.tareas[tarea.id] = tarea

    def asignar_tarea(self, tarea_id, empleado: Empleado):
        t = self.tareas[tarea_id]
        t.asignado = empleado

    def calcular_cronograma(self):
   
        resolved = {}
        def resolve(t):
            if t.id in resolved:
                return resolved[t.id]
            if not t.dependencias:
                inicio = self.fecha_inicio
            else:
                fines = []
                for dep_id in t.dependencias:
                    dep = self.tareas[dep_id]
                    fin_dep = resolve(dep)[1]
                    fines.append(fin_dep)
                inicio = max(fines)
            fin = inicio + timedelta(days=t.duracion)
            t.inicio_estimado = inicio
            t.fin_estimado = fin
            resolved[t.id] = (inicio, fin)
            return resolved[t.id]

        for t in self.tareas.values():
            if t.id not in resolved:
                resolve(t)

    def estado_general(self):
        estados = {}
        for t in self.tareas.values():
            estados[t.titulo] = t.estado
        return estados

if __name__ == "__main__":
    p = Proyecto("Lanzamiento Web", datetime(2025, 10, 1))
    t1 = Tarea("Diseño UI", 5)
    t2 = Tarea("Frontend", 10)
    t3 = Tarea("Backend", 12)
    t4 = Tarea("Integración", 3)

    t2.agregar_dependencia(t1)
    t3.agregar_dependencia(t1)
    t4.agregar_dependencia(t2)
    t4.agregar_dependencia(t3)

    p.agregar_tarea(t1)
    p.agregar_tarea(t2)
    p.agregar_tarea(t3)
    p.agregar_tarea(t4)

    p.calcular_cronograma()
    for t in p.tareas.values():
        print(t.titulo, "-> inicio:", t.inicio_estimado.date(), "fin:", t.fin_estimado.date())
