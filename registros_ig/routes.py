from registros_ig import app
from flask import render_template, request, redirect  

@app.route("/")
def hello():
    diccionario = [{"fecha":"2024-01-01", "concept":"Nomina Enero", "monto":1500},
                   {"fecha":"2024-01-02", "concept":"Compra de reyes", "monto":-100},
                   {"fecha":"2024-01-03", "concept":"Compra del mercadona", "monto":-100},
                   {"fecha":"2024-01-04", "concept":"Compra de roscon", "monto":-50}]
    return render_template("Index.html", variable = diccionario)