class Temperatura:
    def __init__(self, valor: float, unidad: str):
        self.unidad = unidad.lower()
        if self.unidad == 'c':
            self.celsius = valor
        elif self.unidad == 'f':
            self.celsius = (valor - 32) * 5 / 9
        elif self.unidad == 'k':
            self.celsius = valor - 273.15
        else:
            raise ValueError("Unidad no válida. Usa 'C' para Celsius, 'F' para Fahrenheit o 'K' para Kelvin.")

    def a_celsius(self) -> float:
        return self.celsius
    def a_fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32
    def a_kelvin(self) -> float:
        return self.celsius + 273.15
    def __str__(self):
        return (f"{self.celsius:.2f} °C | "
                f"{self.a_fahrenheit():.2f} °F | "
                f"{self.a_kelvin():.2f} K")
    
t = Temperatura(100, 'C')
print(t) 
t2 = Temperatura(32, 'F')
print(t2)  
t3 = Temperatura(273.15, 'K')
print(t3) 
