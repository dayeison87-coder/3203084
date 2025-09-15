num = 123456789
contador = 0
while num > 0:
    num //= 10
    contador += 1
print("Cantidad de dígitos:", contador)