numeros = []
for i in range(8):
    numeros.append(int(input(f"Número {i+1}: ")))
print("Suma:", sum(numeros))
print("Promedio:", sum(numeros)/len(numeros))
print("Mayor:", max(numeros))