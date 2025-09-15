contraseña= "abc123"
longitud_minima= 8
print("Contraseña:", contraseña)
print(f"Longitud mínima requerida: {longitud_minima}")
if len(contraseña) >= longitud_minima:
    print("Contraseña válida")
else:
    print("Contraseña inválida, debe tener al menos", longitud_minima, "caracteres")
