dic = {"feliz": "😊", "triste": "😢", "enojado": "😡", "amor": "❤️"}
estado = input("Ingrese estado de ánimo: ")
print("Emoji correspondiente:", dic.get(estado, "No disponible"))
