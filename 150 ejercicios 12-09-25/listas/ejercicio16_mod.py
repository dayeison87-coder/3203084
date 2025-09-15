#Mostrar los numeros mayores que el promedio

numeros = [10, 20, 30, 40, 50,]
promedio = (10 + 20 + 30 + 40 + 50) / 5
mayores = []
if numeros [0] > promedio:
    mayores.append(numeros[0])
    if numeros [1] > promedio:
        mayores.append(numeros[1])
    if numeros [2] > promedio:
        mayores.append(numeros[2])
    if numeros [3] > promedio:
        mayores.append(numeros[3])
        if numeros [4] > promedio:
            mayores.append(numeros[4])

print ("promedio:", promedio)
print ("Mayores al promedio:", mayores)