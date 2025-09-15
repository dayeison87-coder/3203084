dic = {"py": "Python", "js": "JavaScript", "java": "Java", "cpp": "C++"}
codigo = input("Ingrese código (py, js, java, cpp): ")
print("Lenguaje:", dic.get(codigo, "No encontrado"))
