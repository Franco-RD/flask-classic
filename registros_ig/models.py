import sqlite3 as sq

con = sq.connect("db_movimientos.sqlite")
cur = con.cursor()

def select_all():
    diccionario = [{"date":"2024-01-01", "concept":"Nomina Enero", "quantity":1500},
                    {"date":"2024-01-02", "concept":"Compra de reyes", "quantity":-100},
                    {"date":"2024-01-03", "concept":"Compra del mercadona", "quantity":-100},
                    {"date":"2024-01-04", "concept":"Compra de roscon", "quantity":-50}]

    return diccionario