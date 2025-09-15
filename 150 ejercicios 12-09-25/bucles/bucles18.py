# 1. Imprimir números del 1 al 10 con explicación
print("Números del 1 al 10:")
for i in range(1, 11):
    print(f"El número actual es: {i}")
print("Fin del bucle.\n")

# 2. Imprimir números pares del 2 al 20
print("Números pares del 2 al 20:")
for i in range(2, 21, 2):
    print(f"{i} es par")
print("Fin del bucle.\n")

# 3. Imprimir números impares del 1 al 19
print("Números impares del 1 al 19:")
for i in range(1, 20, 2):
    print(f"{i} es impar")
print("Fin del bucle.\n")

# 4. Tabla de multiplicar del 5
print("Tabla de multiplicar del 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
print("Fin de la tabla.\n")

# 5. Contar regresivamente del 10 al 1
print("Cuenta regresiva del 10 al 1:")
for i in range(10, 0, -1):
    print(i)
print("¡Despegue!\n")

# 6. Imprimir cada letra de una palabra
palabra = "Python"
print(f"Mostrando cada letra de la palabra '{palabra}':")
for letra in palabra:
    print(f"Letra: {letra}")
print("Fin de palabra.\n")

# 7. Sumar los números del 1 al 100
suma = 0
for i in range(1, 101):
    suma += i
print("La suma de los números del 1 al 100 es:", suma, "\n")

# 8. Imprimir cuadrados de los números del 1 al 10
print("Cuadrados del 1 al 10:")
for i in range(1, 11):
    print(f"El cuadrado de {i} es {i**2}")
print("Fin del cálculo.\n")

# 9. Imprimir una lista de frutas con sus posiciones
frutas = ["Manzana", "Banano", "Pera", "Uva"]
print("Lista de frutas:")
for i in range(len(frutas)):
    print(f"Fruta {i+1}: {frutas[i]}")
print("Fin de lista.\n")

# 10. Mostrar los múltiplos de 3 hasta 30 con conteo
print("Múltiplos de 3 hasta 30:")
contador = 0
for i in range(3, 31, 3):
    contador += 1
    print(f"Múltiplo {contador}: {i}")
print("Fin de los múltiplos.\n")
