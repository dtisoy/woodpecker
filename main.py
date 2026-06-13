import menu
import administrador_ciclos


def crear_nuevo_entrenamiento():

    administrador_ciclos.configuracion_inicial()
    administrador_ciclos.comenzar_ciclo(semanas=4)
    print("¡Entrenamiento creado exitosamente!")


existe_entrenamiento = administrador_ciclos.validar_existencia_entrenamiento()
opcion = menu.mostrar_menu_principal(existe_entrenamiento)

match opcion:
    case "1":
        crear_nuevo_entrenamiento()
        administrador_ciclos.abrir_sesion_entrenamiento()
    case _:
        print("saliendo")
