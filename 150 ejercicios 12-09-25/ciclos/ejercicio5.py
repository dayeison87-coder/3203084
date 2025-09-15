inicio = int(input("Ingresa el número inicial: "))
fin = int(input("Ingresa el número final: "))

primos = []


for num in range(inicio, fin + 1):
    if num > 1:  
        es_primo = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)


print(f"\nNúmeros primos entre {inicio} y {fin}:")
print(primos)