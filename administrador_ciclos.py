from datetime import timedelta, datetime as dt
import csv
from os.path import exists

archivo_fechas = "historial_ciclos"
archivo_lista_puzzles = "lista_puzzles_entrenamiento"


def comenzar_ciclo(ciclo=1, semanas=0, dias=0):

    hoy = dt.now()
    # no es necesaria la hora
    fecha_inicio = dt(year=hoy.year, month=hoy.month, day=hoy.day)
    fecha_final = fecha_inicio + timedelta(weeks=semanas, days=dias)

    fecha_ini_str = fecha_inicio.strftime("%Y-%m-%d")
    fecha_fin_str = fecha_final.strftime("%Y-%m-%d")
    datos = [ciclo, fecha_ini_str, fecha_fin_str]

    with open(archivo_fechas, "a") as f:
        escritor = csv.writer(f)
        escritor.writerow(datos)


def configuracion_inicial():
    # archivo de ciclos
    encabezado = ["ciclo", "fecha inicio", "fecha fin"]
    with open(archivo_fechas, "w") as f:
        escritor = csv.writer(f, delimiter=",")
        escritor.writerow(encabezado)

    # historial de puzzles
    with open(archivo_lista_puzzles, "w") as f:
        escritor = csv.writer(f, delimiter=",")
        escritor.writerow(["puzzle id", "rating"])


def validar_existencia_entrenamiento():
    return exists(archivo_fechas) and exists(archivo_lista_puzzles)


def obtener_puzzles(nombre_archivo):
    # si el ciclo es 1, se trae la lista de puzzles de lichess
    with open(nombre_archivo, "r") as f:
        lector = csv.reader(f)
        filas = list(lector)
    return list(enumerate(filas))


def obtener_ultimo_puzzle():
    # ultimo puzzle resuelto
    with open(archivo_lista_puzzles, "r") as f:
        lector = csv.reader(f)
        filas = list(lector)
    return len(filas) - 1


def formato_url_puzzle(puzzle_id):
    return f"https://lichess.org/training/{puzzle_id}"


def guardar_puzzle(data):
    with open(archivo_lista_puzzles, "a", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(data)


def abrir_sesion_entrenamiento():
    # optener fecha final del ultimo ciclo:
    with open(archivo_fechas, "r") as f:
        lector = csv.reader(f)
        filas = list(lector)
        ciclo_actual = filas[-1]
    # ciclo: 0, inicio: 1, fin: 2
    fecha_fin = ciclo_actual[2]
    # definir que archivos se va a usar:
    if int(ciclo_actual[0]) == 1:
        f_lista_puzzles = "filtered_puzzles.csv"
    else:
        f_lista_puzzles = archivo_lista_puzzles
    fecha_fin = dt.strptime(fecha_fin, "%Y-%m-%d")
    hoy = dt.now()
    if fecha_fin >= hoy:
        # ultimo puzzle resuelto
        ultimo_puzzle_idx = obtener_ultimo_puzzle() + 1
        puzzles = obtener_puzzles(f_lista_puzzles)

        contador = ultimo_puzzle_idx
        while contador < len(puzzles):
            puzzle_data = puzzles[contador][1]
            contador += 1
            puzzle_id = puzzle_data[0]
            print(formato_url_puzzle(puzzle_id))
            # FIXME: escribir en el archivo una vez que se termine la sesion de entrenamiento
            # FIXME: si # ciclo > 1 entonces ya no se escribe en el archivo lista puzzles entrenamiento
            guardar_puzzle(puzzle_data)
            continua = input(
                "Presione Enter para el siguiente puzzle, 'q' para salir..."
            )
            if continua == "q":
                # TODO: mostrar "estadisticas" del set actual
                break
    elif hoy > fecha_fin:
        pass
        # TODO: crear un nuevo ciclo
        # TODO: settear el archivo lista de puzzles como referencia


# if __name__ == "__main__":
    # abrir_sesion_entrenamiento()
    # comenzar_ciclo(ciclo=2, semanas=2)
