import sqlite3
from registros_ig import ORIGIN_DATA


def select_all():
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute("select * from movements;")  #res es como un objeto gigante con un monton de cosas
    filas = res.fetchall()  #res.fetchall() si trae los datos de las columnas nada mas en un a lista de tuplas (1, 2024-01-01, Nomina Enero, 1500)
    columnas = res.description  #Nombres de columnas en lista de tuplas  (id,0000) (date,0000) (concept,0000) (quantity,0000)

    lista_diccionario = []
    
    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]  # c es cada tupla de (nombre columna, 0000), la posicion 0 es el nombre de la columna. f es una tupla con todos los datos de una fila, por eso va cambiando con posicion. 
            posicion += 1                    # En cada iteracion de este for agrega al diccionario el nombre de la columna como clave y el valor de f[posicion]. 
                                             # Cuando termina este for de agregar todos los datos de una fila al diccionario, lo agrega a la lista de diccionarios y pasa a la siguiente fila.
        lista_diccionario.append(diccionario)

    conexion.close()
    return lista_diccionario


def insert(registroForm):
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute("insert into movements (date, concept, quantity) values (?,?,?);", registroForm)  #Se puede poner ? y luego de la ", se ponen los registros en orden que irian en esos campos. registroForm ya tiene los 3 datos ya que es una lista
    conexion.commit()  #Valida los INSERT. Cuando se hacen INSERT hay que usarlo. Hasta que no se hace el commit no se mandan los insert que hagamos
    conexion.close()


def select_by(id):
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute(f"select * from movements where id={id};")
    result = res.fetchall()
    return result[0]