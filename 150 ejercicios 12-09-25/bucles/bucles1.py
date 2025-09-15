# 18. Calcular factorial de un número
print("Cálculo de factorial:")
n = int(input("Ingrese un número: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    print(f"Multiplicando por {i}, factorial ahora es {factorial}")
    i += 1
print(f"El factorial de {n} es {factorial}\n")