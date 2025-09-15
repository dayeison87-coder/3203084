def saludar(nombre): 
	"""Esta función saluda a una persona por su nombre"""
	mensaje = f"¡Hola {nombre}! ¿Cómo estás?"
	return mensaje 
saludo1 = saludar("Ana") 
saludo2 = saludar("Carlos") 
saludo3 = saludar("María") 
print("Usando mi función de saludo:")
print(saludo1)
print(saludo2)
print(saludo3)
print("\nUsando directamente:")
print(saludar("Pedro"))
print(saludar("Laura"))
