dic = {"USD": 4000, "EUR": 4500, "MXN": 250}
moneda = input("Ingrese código de moneda (USD, EUR, MXN): ")
print("Tasa en pesos colombianos:", dic.get(moneda, "No registrada"))
