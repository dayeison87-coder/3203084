import math
def calculadora():
    while True:
        print("\dato--- CALCULADORA CIENTÍFICA ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Raíz cuadrada")
        print("7. Factorial")
        print("0. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "0":
            break
        if opcion in ["1", "2", "3", "4", "5"]:
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
        if opcion == "1":
            print("Resultado:", a + b)
        elif opcion == "2":
            print("Resultado:", a - b)
        elif opcion == "3":
            print("Resultado:", a * b)
        elif opcion == "4":
            if b != 0:
                print("Resultado:", a / b)
            else:
                print("Error: División por cero")
        elif opcion == "5":
            print("Resultado:", a ** b)
        elif opcion == "6":
            varx = float(input("Número: "))
            print("Resultado:", math.sqrt(varx))
        elif opcion == "7":
            dato = int(input("Número entero: "))
            print("Resultado:", math.factorial(dato))
        else:
            print("Opción no válida")
if __name__ == "__main__":
    calculadora()
