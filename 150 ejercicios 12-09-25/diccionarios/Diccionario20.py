dic = {"🇨🇴": "Colombia", "🇲🇽": "México", "🇪🇸": "España", "🇦🇷": "Argentina"}
bandera = input("Ingrese un emoji de bandera: ")
print("País:", dic.get(bandera, "No encontrado"))
