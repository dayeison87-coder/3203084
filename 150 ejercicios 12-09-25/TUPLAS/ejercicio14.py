dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
n = int(input("Ingresa un número del 1 al 7: "))
if 1 <= n <= 7:
    print("Ese día es:", dias[n-1])
else:
    print("Número inválido")
