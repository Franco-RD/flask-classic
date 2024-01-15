import sqlite3
from registros_ig import ORIGIN_DATA
from registros_ig.conexion import Conexion

def select_all():
    conectar = Conexion("select * from movements")
    filas = conectar.res.fetchall()  #res.fetchall() si trae los datos de las columnas nada mas en un a lista de tuplas (1, 2024-01-01, Nomina Enero, 1500)
    columnas = conectar.res.description  #Nombres de columnas en lista de tuplas  (id,0000) (date,0000) (concept,0000) (quantity,0000)

    lista_diccionario = []
    
    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]  # c es cada tupla de (nombre columna, 0000), la posicion 0 es el nombre de la columna. f es una tupla con todos los datos de una fila, por eso va cambiando con posicion. 
            posicion += 1                    # En cada iteracion de este for agrega al diccionario el nombre de la columna como clave y el valor de f[posicion]. 
                                             # Cuando termina este for de agregar todos los datos de una fila al diccionario, lo agrega a la lista de diccionarios y pasa a la siguiente fila.
        lista_diccionario.append(diccionario)

    conectar.con.close()
    return lista_diccionario


def insert(registroForm):
    conectarInsert = Conexion("insert into movements (date, concept, quantity) values (?,?,?);", registroForm)
    #cur.execute("insert into movements (date, concept, quantity) values (?,?,?);", registroForm)  #Se puede poner ? y luego de la ", se ponen los registros en orden que irian en esos campos. registroForm ya tiene los 3 datos ya que es una lista
    conectarInsert.con.commit()  #Valida los INSERT. Cuando se hacen INSERT hay que usarlo. Hasta que no se hace el commit no se mandan los insert que hagamos
    conectarInsert.con.close()


def select_by(id):
    conectarSelectBy = Conexion(f"select * from movements where id={id};")
    #res = cur.execute(f"select * from movements where id={id};")  #La asignacion del execute a una variable la usamos cuando buscamos datos que despues vayamos a mostrar. En insert y delete no hacen falta.
    result = conectarSelectBy.res.fetchall()
    conectarSelectBy.con.close()
    return result[0]

#Los cur.execute se comentaron porque pasaron a la clase Conexion, se dejan para el comentario nada mas. 

def delete_by(id):
    conectarDeleteBy = Conexion(f"delete from movements where id={id};")
    conectarDeleteBy.con.commit()  #Valida el delete. Cuando se hacen DELETE tambien hay que usarlo sino no se confirma el borrado.
    conectarDeleteBy.con.close()