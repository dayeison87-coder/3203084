# 19. Imprimir los dígitos de un número
print("Mostrar los dígitos de un número:")
num = int(input("Ingrese un número: "))
print(f"Dígitos de {num}:")
while num > 0:
    digito = num % 10
    print(f"Dígito: {digito}")
    num //= 10
print("Fin del bucle.\n")