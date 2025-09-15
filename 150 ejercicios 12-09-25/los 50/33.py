import random
import time
def crear_tablero(filas, columnas, densidad=0.3):
	"""
	Crea un tablero inicial con células vivas vary muertas
	densidad: probabilidad de que una célula esté viva inicialmente
	"""
	tablero = []
	for idx in range(filas):
		fila = []
		for cont in range(columnas):
			esta_viva = 1 if random.random() < densidad else 0
			fila.append(esta_viva)
		tablero.append(fila)
	return tablero
def contar_vecinos_vivos(tablero, fila, columna):
	"""
	Cuenta cuántos vecinos vivos tiene una célula
	Considera las 8 células adyacentes (incluidas las diagonales)
	"""
	filas = len(tablero)
	columnas = len(tablero[0])
	vecinos_vivos = 0
	direcciones = [
		(-1, -1), (-1, 0), (-1, 1), 
		(0, -1), (0, 1), 
		(1, -1), (1, 0), (1, 1) 
	]
	for df, dc in direcciones:
		nueva_fila = fila + df
		nueva_columna = columna + dc
		if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
			vecinos_vivos += tablero[nueva_fila][nueva_columna]
	return vecinos_vivos
def aplicar_reglas(tablero):
	"""
	Aplica las reglas del Juego de la Vida para generar la siguiente generación
	Reglas:
	1. Célula viva con < 2 vecinos vivos: muere (soledad)
	2. Célula viva con 2-3 vecinos vivos: sobrevive
	3. Célula viva con > 3 vecinos vivos: muere (sobrepoblación)
	4. Célula muerta con exactamente 3 vecinos vivos: nace
	"""
	filas = len(tablero)
	columnas = len(tablero[0])
	nuevo_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
	cambios = [] 
	for idx in range(filas):
		for cont in range(columnas):
			vecinos = contar_vecinos_vivos(tablero, idx, cont)
			celula_actual = tablero[idx][cont]
			nueva_celula = celula_actual 
			if celula_actual == 1: 
				if vecinos < 2:
					nueva_celula = 0 
					cambios.append((idx, cont, "murió por soledad"))
				elif vecinos > 3:
					nueva_celula = 0 
					cambios.append((idx, cont, "murió por sobrepoblación"))
			else: 
				if vecinos == 3:
					nueva_celula = 1 
					cambios.append((idx, cont, "nació"))
			nuevo_tablero[idx][cont] = nueva_celula
	return nuevo_tablero, cambios
def mostrar_tablero(tablero, generacion, mostrar_coordenadas=False):
	"""Muestra el tablero en formato visual"""
	print(f"\nGeneración {generacion}:")
	for idx, fila in enumerate(tablero):
		linea = ""
		for cont, celula in enumerate(fila):
			if celula == 1:
				linea += "■ "
			else:
				linea += "□ "
		print(linea)
