

def mostrar_menu_principal(existe_entre = False):
    print("\t¡Bienvenido a woodpecker!".upper())
    print()
    print("1. Generar nuevo ciclo de entrenamiento")
    if existe_entre:
        print("2. Iniciar sesión de puzzles (ciclo actual)")
    print()
    print("Presionar cualquier tecla para salir")

    opcion = input("Seleccione una opción: ")

    return opcion

