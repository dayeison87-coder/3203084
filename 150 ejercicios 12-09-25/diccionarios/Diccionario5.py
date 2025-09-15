dic = {"Ana": 4.5, "Pedro": 3.8, "Luis": 4.0, "María": 4.9}
est = input("Ingrese nombre del estudiante: ")
print("Su nota es:", dic.get(est, "No encontrado"))
