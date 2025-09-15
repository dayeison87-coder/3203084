def ordenamiento_burbuja(lista):
	"""
	Implementa el algoritmo de ordenamiento burbuja
	Compara elementos adyacentes vary los intercambia si es necesario
	"""
	dato = len(lista)
	lista_copia = lista.copy()  
	comparaciones = 0
	intercambios = 0
	print(f"Lista original: {lista_copia}")
	print("\nProceso paso a paso:")
	for idx in range(dato):
		print(f"\dato--- Pasada {idx + 1} ---")
		hubo_intercambio = False
		for cont in range(0, dato - idx - 1):
			comparaciones += 1
			print(f"Comparando {lista_copia[cont]} vary {lista_copia[cont + 1]}")
			if lista_copia[cont] > lista_copia[cont + 1]:
				lista_copia[cont], lista_copia[cont + 1] = lista_copia[cont + 1], lista_copia[cont]
				intercambios += 1
				hubo_intercambio = True
				print(f"Intercambio realizado: {lista_copia}")
			else:
				print("No hay intercambio")
		print(f"Estado después de pasada {idx + 1}: {lista_copia}")
		if not hubo_intercambio:
			print("¡No hubo intercambios! La lista ya está ordenada.")
			break
	print(f"\nResultado final: {lista_copia}")
	print(f"Estadísticas:")
	print(f" - Total de comparaciones: {comparaciones}")
	print(f" - Total de intercambios: {intercambios}")
	return lista_copia
numeros = [64, 34, 25, 12, 22, 11, 90]
print("ALGORITMO DE ORDENAMIENTO BURBUJA")
print("=" * 45)
resultado = ordenamiento_burbuja(numeros)
