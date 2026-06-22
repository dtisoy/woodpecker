

def mostrar_menu_principal(existe_entre = False):
    title ="¡Bienvenido a woodpecker!" 
    margen = "="*(len(title)+16)
    print()
    print(margen)
    print("\t"+title.upper())
    print(margen)
    print()

    print("1. Generar nuevo ciclo de entrenamiento")
    if existe_entre:
        print("2. Iniciar sesión de puzzles (ciclo actual)")
    print()
    print("Presionar cualquier tecla para salir")
    print()
    opcion = input("Seleccione una opción: ")

    return opcion

