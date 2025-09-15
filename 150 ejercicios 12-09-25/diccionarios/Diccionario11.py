dic = {"Futbol": 11, "Baloncesto": 5, "Voleibol": 6, "Tenis": 1}
dep = input("Ingrese deporte: ")
print("Número de jugadores por equipo:", dic.get(dep, "No registrado"))
