from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar_permisos(self):
        pass


class Administrador(Usuario):
    def mostrar_permisos(self):
        print(f"Administrador {self.nombre}: puede gestionar usuarios, editar y eliminar todo el contenido.")


class Cliente(Usuario):
    def mostrar_permisos(self):
        print(f"Cliente {self.nombre}: puede navegar, comprar productos y dejar reseñas.")


class Moderador(Usuario):
    def mostrar_permisos(self):
        print(f"Moderador {self.nombre}: puede supervisar comentarios y moderar el contenido de la comunidad.")


if __name__ == "__main__":
    usuarios = [
        Administrador("Ana"),
        Cliente("Carlos"),
        Moderador("Lucía")
    ]

    for u in usuarios:
        u.mostrar_permisos()
