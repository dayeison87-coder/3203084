dic = {"Colombia": "Bogotá", "Perú": "Lima", "México": "Ciudad de México", "España": "Madrid"}
pais = input("Ingrese un país: ")
print("Su capital es:", dic.get(pais, "No registrado"))
