# 13. Pedir números hasta que el usuario ingrese 0
print("Ingrese números (escriba 0 para salir):")
num = int(input("Número: "))
while num != 0:
    print(f"Ingresaste: {num}")
    num = int(input("Número: "))
print("Has salido del programa.\n")