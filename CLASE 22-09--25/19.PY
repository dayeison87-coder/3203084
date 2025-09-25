from abc import ABC, abstractmethod

class ElementoSistema(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar(self, nivel=0):
        pass


class Archivo(ElementoSistema):
    def mostrar(self, nivel=0):
        print("  " * nivel + f"- Archivo: {self.nombre}")


class Carpeta(ElementoSistema):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.elementos = []  

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"+ Carpeta: {self.nombre}")
        for elemento in self.elementos:
            elemento.mostrar(nivel + 1)



if __name__ == "__main__":
    raiz = Carpeta("Proyecto")

    carpeta_src = Carpeta("src")
    carpeta_src.agregar(Archivo("main.py"))
    carpeta_src.agregar(Archivo("util.py"))

    carpeta_docs = Carpeta("docs")
    carpeta_docs.agregar(Archivo("manual.txt"))

    raiz.agregar(carpeta_src)
    raiz.agregar(carpeta_docs)
    raiz.agregar(Archivo("README.md"))

  
    raiz.mostrar()