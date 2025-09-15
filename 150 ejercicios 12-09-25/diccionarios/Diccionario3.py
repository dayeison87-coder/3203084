dic = {"suma": "+", "resta": "-", "multi": "*", "div": "/"}
print(dic)

a = int(input("Primer número: "))
b = int(input("Segundo número: "))
op = input("Elige operación (suma, resta, multi, div): ")

if op == "suma":
    print("Resultado:", a+b)
elif op == "resta":
    print("Resultado:", a-b)
elif op == "multi":
    print("Resultado:", a*b)
elif op == "div":
    print("Resultado:", a/b if b!=0 else "Error: división por cero")
