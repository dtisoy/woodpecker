import menu
import administrador_ciclos


def crear_nuevo_entrenamiento():

    administrador_ciclos.configuracion_inicial()
    administrador_ciclos.comenzar_ciclo(semanas=4)

    mensaje ="[+] ¡Entrenamiento creado exitosamente!" 
    margen = "-"*(len(mensaje))
    print()
    print(mensaje)
    print()


existe_entrenamiento = administrador_ciclos.validar_existencia_entrenamiento()
opcion = menu.mostrar_menu_principal(existe_entrenamiento)

def main():
    # FIXME: usar un bucle while para no salirse del programa
    match opcion:
        case "1":
            crear_nuevo_entrenamiento()
            administrador_ciclos.abrir_sesion_entrenamiento()
        case "2":
            administrador_ciclos.abrir_sesion_entrenamiento()
        case _:
            print("saliendo")

main()
