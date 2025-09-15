
while True:
    mensaje = input("Tú: ")
    if mensaje.lower() == "salir":
        print("Chat cerrado 👋")
        break
    print("Bot:", mensaje)