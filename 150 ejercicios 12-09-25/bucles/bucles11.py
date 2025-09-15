# 10. Mostrar los múltiplos de 3 hasta 30 con conteo
print("Múltiplos de 3 hasta 30:")
contador = 0
for i in range(3, 31, 3):
    contador += 1
    print(f"Múltiplo {contador}: {i}")
print("Fin de los múltiplos.\n")