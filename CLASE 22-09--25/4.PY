class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar(self, tarea):
        self.tareas.append([tarea, False])

    def eliminar(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)

    def completar(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice][1] = True

    def mostrar(self):
        for i, (tarea, hecha) in enumerate(self.tareas):
            estado = "✔" if hecha else "✗"
            print(f"{i}. {tarea} [{estado}]")

# Ejemplo de uso
lista = ListaTareas()
lista.agregar("Estudiar")
lista.agregar("Leer")
lista.mostrar()
lista.completar(0)
lista.mostrar()
lista.eliminar(1)
lista.mostrar()