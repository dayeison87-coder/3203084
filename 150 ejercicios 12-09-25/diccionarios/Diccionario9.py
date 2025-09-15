dic = {"admin": "1234", "user": "abcd", "guest": "0000"}
user = input("Ingrese usuario: ")
clave = input("Ingrese contraseña: ")

if dic.get(user) == clave:
    print("Acceso permitido")
else:
    print("Acceso denegado")
