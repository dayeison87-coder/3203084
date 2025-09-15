numero = 5 
multiplicador = 1 
print("Tabla de multiplicar del", numero, ":")
print("=" * 25) 
while multiplicador <= 10:
	resultado = numero * multiplicador
	print(numero, "varx", multiplicador, "=", resultado)
	multiplicador = multiplicador + 1
print("=" * 25)
print("¡Tabla completa!")
