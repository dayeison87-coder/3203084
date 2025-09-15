vars="xxxx"
print(id(vars))

bar1=vars
print(id(bar1))
print(id(vars))

class vehiculo:
    def __init__(self, motor, ruedas, capacidad):
        self.motor="200hp"
        self.ruedas="15p"
        self.capacidad="4"

coche1=vehiculo("200hp","15p","4")
print(coche1.motor)
print(coche1.ruedas)
print(coche1.capacidad)

class universidad:
    def __init__(self, nombre, direccion, telefono):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono

clase1=universidad("UTN","Av. Siempre Viva 123","123456789")
print(clase1.nombre)    
print(clase1.direccion)
print(clase1.telefono) 


class zoo:
    def __init__(self, resinto, criatura, tipo):
        self.resinto=resinto
        self.criatura=criatura
        self.tipo=tipo
zoo1=zoo("A","Leon","Mamifero")
print(zoo1.resinto)     
print(zoo1.criatura)
print(zoo1.tipo)


class restaurante:
    def __init__(self, sopa, plato_fuerte, postre):
        self.nombre=sopa
        self.direccion=plato_fuerte
        self.telefono=postre
        
restaurante1=restaurante("Minestrone","Bife de chorizo","Helado")
print(restaurante1.nombre)  
print(restaurante1.direccion)
print(restaurante1.telefono)    
    
       
class Persona:
    def __new__(cls, nombre , edad):
        return super().__new__(cls)

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        pass


ana = Persona("Ana", 30)
carlos = Persona("Carlos", 49)

print(f"{ana.nombre}, {ana.edad}, {carlos.nombre}, {carlos.edad}")
