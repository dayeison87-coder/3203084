dic = {1: "Uno", 2: "Dos", 3: "Tres", 4: "Cuatro"}
num = int(input("Ingrese un número (1-4): "))
print("En palabras:", dic.get(num, "No existe"))
