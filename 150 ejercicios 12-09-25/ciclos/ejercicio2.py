n = int(input("Hasta qué número: "))
for i in range(1, n+1):
    print(f"{i} en binario es {bin(i)[2:]}")