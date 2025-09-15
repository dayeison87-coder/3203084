texto=input("escribe un texto aqui")
contador = 0
for i in texto:
    if i != " ,":
        contador += 1

print("esta es la cantidad de caracteres: ", contador)