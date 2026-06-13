from datetime import timedelta, datetime as dt
import csv
from os.path import exists

archivo_fechas = "historial_ciclos"
set_puzzles = "filtered_puzzles.csv"


def configuracion_inicial():
    # archivo de ciclos
    encabezado = ["ciclo", "fecha inicio", "fecha fin", "# puzzles resueltos"]
    with open(archivo_fechas, "w") as f:
        escritor = csv.writer(f, delimiter=",")
        escritor.writerow(encabezado)


def comenzar_ciclo(ciclo=1, semanas=4, dias=0):

    hoy = dt.now()
    # no es necesaria la hora
    fecha_inicio = dt(year=hoy.year, month=hoy.month, day=hoy.day)
    fecha_final = fecha_inicio + timedelta(weeks=semanas, days=dias)

    fecha_ini_str = fecha_inicio.strftime("%Y-%m-%d")
    fecha_fin_str = fecha_final.strftime("%Y-%m-%d")

    puzzles_resueltos = 0

    datos = [ciclo, fecha_ini_str, fecha_fin_str, puzzles_resueltos]

    with open(archivo_fechas, "a", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(datos)


def validar_existencia_entrenamiento():
    return exists(archivo_fechas)


def obtener_historial_ciclos():
    with open(archivo_fechas, "r") as f:
        lector = csv.reader(f)
        filas = list(lector)
    return filas


def obtener_info_ciclo_actual():

    info_general = obtener_historial_ciclos()
    ciclo_actual = info_general[-1]

    # # ciclo: 0, inicio: 1, fin: 2, # puzzles: 3
    fecha_inicio = dt.strptime(ciclo_actual[1], "%Y-%m-%d")
    fecha_fin = dt.strptime(ciclo_actual[2], "%Y-%m-%d")

    # determinar el limite de puzzles a resolver en el ciclo actual
    cantidad = 0 if int(ciclo_actual[0]) == 1 else int(info_general[-2][3])
    data = {
        "ciclo": int(ciclo_actual[0]),
        "inicio": fecha_inicio,
        "fin": fecha_fin,
        "puzzles_resueltos": int(ciclo_actual[3]),
        "limite_puzzles": cantidad,
    }

    return data


def actualizar_info_ciclo_actual(puzzles_resueltos):

    # WARNING: lo unico que se actualiza es el numero de puzzles resueltos
    info_general = obtener_historial_ciclos()
    # # ciclo: 0, inicio: 1, fin: 2, # puzzles: 3
    info_general[-1][3] = puzzles_resueltos

    with open(archivo_fechas, "w") as f:
        escritor = csv.writer(f)
        escritor.writerows(info_general)


def obtener_puzzles():

    with open(set_puzzles, "r") as f:
        lector = csv.reader(f)
        filas = list(lector)
        filas.pop(0)
    return list(enumerate(filas))


def formato_url_puzzle(puzzle_id):
    return f"https://lichess.org/training/{puzzle_id}"


def crear_entrenamiento_estatico():
    # TODO: reducir el ciclo anterior a la mitad
    # ciclo 1 = 4, ciclo 2 = 2, ciclo 3 = 1, ciclo 4 = 6 dias, ciclo 5 = 3 dias, ciclo 6 = 1 dia
    # obtener ultimo ciclo
    ultimo_ciclo = obtener_info_ciclo_actual()
    numero_ciclo = ultimo_ciclo["ciclo"]
    # en futuras versiones puede ser dinamico
    match numero_ciclo:
        case 1:
            comenzar_ciclo(ciclo=2, semanas=2)
        case 2:
            comenzar_ciclo(ciclo=3, semanas=1)
        case 3:
            comenzar_ciclo(ciclo=4, dias=6)
        case 4:
            comenzar_ciclo(ciclo=5, dias=3)
        case 5:
            comenzar_ciclo(ciclo=6, dias=1)


def abrir_sesion_entrenamiento():
    ciclo_actual = obtener_info_ciclo_actual()

    hoy = dt.now()
    if ciclo_actual["fin"] < hoy:
        print(f"Se ha iniciado el ciclo de entrenamiento {ciclo_actual["ciclo"]+1} ")
        crear_entrenamiento_estatico()
        # se usará el nuevo ciclo creado
        ciclo_actual = obtener_info_ciclo_actual()
    # FIXME: este if se puede eliminar
    if ciclo_actual["fin"] >= hoy:
        # ultimo puzzle resuelto
        ultimo_puzzle = ciclo_actual["puzzles_resueltos"]

        puzzles = obtener_puzzles()

        cantidad_puzzles = (
            ciclo_actual["limite_puzzles"]
            if ciclo_actual["limite_puzzles"]
            else len(puzzles)
        )

        contador = ultimo_puzzle
        while contador < cantidad_puzzles:
            # TODO: si el ciclo es > 1 entonces los puzzles se limitan a los # puzzles resueltos del ciclo anterior
            puzzle_data = puzzles[contador][1]
            contador += 1
            puzzle_id = puzzle_data[0]
            print(formato_url_puzzle(puzzle_id))

            continua = input(
                "Presione Enter para el siguiente puzzle, 'q' para salir..."
            )
            if continua == "q":
                # TODO: mostrar "estadisticas" del set actual
                actualizar_info_ciclo_actual(contador)
                break
        actualizar_info_ciclo_actual(contador)
        if contador == cantidad_puzzles:

            print("Felicidades haz completado el set de puzzles para este ciclo")

        else:
            print("Haz terminado tu sesion de entrenamiento")
            print("Saliendo")
