dic = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes", 6: "Sábado", 7: "Domingo"}
num = int(input("Ingrese un número (1-7): "))
print("Día:", dic.get(num, "Número inválido"))
