dic = {"hello": "hola", "bye": "adiós", "cat": "gato", "dog": "perro"}
palabra = input("Ingrese palabra en inglés: ")
print("Traducción:", dic.get(palabra, "No encontrada"))
