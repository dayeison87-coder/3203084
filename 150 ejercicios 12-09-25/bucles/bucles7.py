# 14. Sumar números hasta que la suma supere 50
print("Suma de números hasta superar 50:")
suma = 0
while suma <= 50:
    num = int(input("Ingrese un número: "))
    suma += num
    print(f"Suma actual: {suma}")
    print("La suma superó 50. Fin del programa.\n")