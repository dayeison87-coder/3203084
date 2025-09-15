frase = input("Escribe una frase: ")
letras = numeros = 0
for ch in frase:
    if ch.isalpha():
        letras += 1
    elif ch.isdigit():
        numeros += 1
print("Letras:", letras, "Números:", numeros)