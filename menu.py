

def mostrar_menu_principal(existe_entre = False):
    print("\t¡Bienvenido a woodpecker!".upper())
    print()
    print("(1) Comenzar nuevo entrenamiento")
    if existe_entre:
        print("(2) Continuar entrenamiento")
    print()
    print("Presionar cualquier tecla para salir")

    opcion = input("Ingresa una opcion: ")

    return opcion

def mostrar_menu_nuevo_entrenamiento(): 
    print()
    print("Ingresa el numero de semanas del ciclo inicial. (por defecto 4 semanas)")
    semanas = input("Presiona enter para la configuracion por defecto: ")
    return semanas
