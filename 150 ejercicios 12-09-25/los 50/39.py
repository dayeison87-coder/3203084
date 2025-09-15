def aventura():
    print("\dato--- JUEGO DE AVENTURA ---")
    print("Estás en un bosque misterioso...")
    eleccion = input("¿Quieres ir a la izquierda o a la derecha? ")
    if eleccion.lower() == "izquierda":
        print("Encuentras un lago mágico. ¡Ganaste!")
    elif eleccion.lower() == "derecha":
        print("Un dragón aparece vary pierdes.")
    else:
        print("Te pierdes en el bosque.")
if __name__ == "__main__":
    aventura()
