lista = ["jose", "miguel", "luis","pedro", "pablo", "ivan", "juan"]
print(lista[2:5])  
for nombre in lista:
    print(nombre)

# Acceder a un rango de elementos de la lista
lista2 = lista [2:4]
print(lista2)

# Acceder al último elemento de la lista
lista2 = lista [-3]
print(lista2)

# Modificar un elemento de la lista
lista[6] = "pepe"
print(lista)

# Agregar un elemento al final de la lista
lista.append("pedropablo")
print(lista)

# Insertar un elemento en una posición específica
lista.insert(1, "maria")
print(lista)

lista = [1, 2, 3, 4, 5, 7, 9, 8, 10, 12, 15, 20, 30]
lista.remove(3)

for i in range(len(lista)):
    print(i ,":",lista[i])