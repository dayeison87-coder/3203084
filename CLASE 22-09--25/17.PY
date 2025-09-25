class Empleado:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado

    def calcular_salario(self):
        raise NotImplementedError("Este método debe ser implementado por las clases hijas.")

    def __str__(self):
        return f"Empleado: {self.nombre} (ID: {self.id_empleado})"

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, id_empleado, salario_mensual):
        super().__init__(nombre, id_empleado)
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual
class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, id_empleado, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, id_empleado)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.pago_por_hora
emp1 = EmpleadoTiempoCompleto("Ana Gómez", 1001, 3000)
emp2 = EmpleadoMedioTiempo("Luis Pérez", 1002, 80, 20)

print(emp1)
print(f"Salario mensual: ${emp1.calcular_salario()}")

print(emp2)
print(f"Salario mensual: ${emp2.calcular_salario()}")
