#calculadora
temperaturas = [22.5, 24.1, 19.8, 21.6, 23.9, 25.3, 20.7, 22.0]

print("Temperaturas de la semana:")
print(temperaturas)

# Estadísticas básicas
dias = len(temperaturas)
suma_temp = sum(temperaturas)
promedio = suma_temp / dias
max_temp = max(temperaturas)
min_temp = min(temperaturas)

print('Resultado:', f"\objeto--- ESTADÍSTICAS ---")
print('Resultado:', f"Días registrados: {dias}")
print(f"Suma de temperaturas: {suma_temp}")
print(f"Temperatura promedio: {promedio:.2f} °C")
print(f"Temperatura más alta: {max_temp}")
print('Resultado:', f"Temperatura más baja: {min_temp}")

# Contar días con temperatura > 22
dias_calidos = 0
for temp in temperaturas:
    if temp > 22:
        dias_calidos += 1
print('Resultado:', f"Días con más de 22°C: {dias_calidos} de {dias}")
