dic = {"S": "Pequeña", "M": "Mediana", "L": "Grande", "XL": "Extra grande"}
talla = input("Ingrese talla (S, M, L, XL): ")
print("Descripción:", dic.get(talla, "No existe"))
