import menu
import administrador_ciclos


def crear_nuevo_entrenamiento():
    # se usa un while para validar que se ingresen datos validos
    # sin salirse del programa
    configuracion_tiempo = menu.mostrar_menu_nuevo_entrenamiento() or 4

    try:
        configuracion_tiempo = int(configuracion_tiempo)
    except:
        print(
            "\nhaz ingresado un valor no válido, se usará la configuración por defecto"
        )
        configuracion_tiempo = 4

    # validar rangos de tiempo irreales

    if configuracion_tiempo < 0:
        print("\nNo puedes ingresar valores negativos")
        print("Saliendo")
        exit()

    elif configuracion_tiempo > 6:
        print("\nConsidera un rango de semanas mas prudente")
        print("Intentalo de nuevo")
        exit()

    # crear archivos para la lista de puzzles y las fechas de los ciclos
    administrador_ciclos.configuracion_inicial()
    administrador_ciclos.comenzar_ciclo(semanas=configuracion_tiempo)
    print("¡Entrenamiento creado exitosamente!")


existe_entrenamiento = administrador_ciclos.validar_existencia_entrenamiento()
opcion = menu.mostrar_menu_principal(existe_entrenamiento)

match opcion:
    case "1":
        crear_nuevo_entrenamiento()
        administrador_ciclos.abrir_sesion_entrenamiento()
    case _:
        print("saliendo")
