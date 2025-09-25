class Leccion:
    def __init__(self, titulo, duracion_min=5):
        self.titulo = titulo
        self.duracion_min = duracion_min
        self.id = str(uuid.uuid4())

class Modulo:
    def __init__(self, titulo):
        self.titulo = titulo
        self.lecciones = []

    def agregar_leccion(self, leccion: Leccion):
        self.lecciones.append(leccion)

class Curso:
    def __init__(self, titulo):
        self.titulo = titulo
        self.modulos = []

    def agregar_modulo(self, mod: Modulo):
        self.modulos.append(mod)

    def total_lecciones(self):
        return sum(len(m.lecciones) for m in self.modulos)

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
  
        self.progreso = set()

    def marcar_completada(self, leccion: Leccion):
        self.progreso.add(leccion.id)

    def progreso_curso(self, curso: Curso):
        total = curso.total_lecciones()
        completadas = 0
        for m in curso.modulos:
            for l in m.lecciones:
                if l.id in self.progreso:
                    completadas += 1
        porcentaje = (completadas / total * 100) if total else 0
        return {"completadas": completadas, "total": total, "porcentaje": porcentaje}

    def puede_certificar(self, curso: Curso, umbral=80):
        return self.progreso_curso(curso)["porcentaje"] >= umbral

if __name__ == "__main__":
    curso = Curso("Python Básico")
    m1 = Modulo("Introducción")
    l1 = Leccion("Qué es Python")
    l2 = Leccion("Instalación")
    m1.agregar_leccion(l1)
    m1.agregar_leccion(l2)
    m2 = Modulo("Control de flujo")
    l3 = Leccion("If/else")
    l4 = Leccion("Bucles")
    m2.agregar_leccion(l3)
    m2.agregar_leccion(l4)

    curso.agregar_modulo(m1)
    curso.agregar_modulo(m2)

    est = Estudiante("Luisa")
    est.marcar_completada(l1)
    est.marcar_completada(l2)
    est.marcar_completada(l3)

    print(est.progreso_curso(curso))
    print("¿Puede certificar (80%)?:", est.puede_certificar(curso, 80))
