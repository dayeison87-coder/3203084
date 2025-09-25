class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            print("Error: No se puede dividir por cero.")
            return None
        return a / b

# Ejemplo de uso
calc = Calculadora()
print("Suma:", calc.sumar(10, 5))
print("Resta:", calc.restar(10, 5))
print("Multiplicación:", calc.multiplicar(10, 5))
print("División:", calc.dividir(10, 0))
print("División válida:", calc.dividir(10, 2))