import sqlite3

def select_all():
    conexion = sqlite3.connect("data/db_movimientos.sqlite")
    cur = conexion.cursor()
    res = cur.execute("select * from movements;")  #res es como un objeto gigante con un monton de cosas
    filas = res.fetchall()  #res.fetchall() si trae los datos de las columnas nada mas en un a lista de tuplas (1, 2024-01-01, Nomina Enero, 1500)
    columnas = res.description  #Nombres de columnas en lista de tuplas  (id,0000) (date,0000) (concept,0000) (quantity,0000)

    lista_diccionario = []
    diccionario = {}
    for f in filas:
        posicion = 0
        for c in columnas:
            diccionario[c[0]] = f[posicion]  # c es cada tupla de (nombre columna, 0000), la posicion 0 es el nombre de la columna. f es una tupla con todos los datos de una fila, por eso va cambiando con posicion. 
            posicion += 1                    # En cada iteracion de este for agrega al diccionario el nombre de la columna como clave y el valor de f[posicion]. 
                                             # Cuando termina este for de agregar todos los datos de una fila al diccionario, lo agrega a la lista de diccionarios y pasa a la siguiente fila.
        lista_diccionario.append(diccionario)
    
    return lista_diccionario

