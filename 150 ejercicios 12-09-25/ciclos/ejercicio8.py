menor, mayor = None, None
for i in range(10):
    n = int(input(f"Número {i+1}: "))
    if menor is None or n < menor:
        menor = n
    if mayor is None or n > mayor:
        mayor = n
print("Menor:", menor, "Mayor:", mayor)
