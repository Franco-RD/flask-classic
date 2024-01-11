from registros_ig import app
from flask import render_template, request, redirect  
from registros_ig.models import *
from datetime import date

def validarFormulario(datosFormulario):
    errores = []
    hoy = str(date.today())  #Fecha del dia para validacion. No se tiene que poder agregar gastos de dias mayores a hoy

    if datosFormulario['date'] > hoy or datosFormulario['date'] == "":
        errores.append("La fecha no puede ser mayor a la actual o vacia")    
    if datosFormulario['concept'] == "":
        errores.append("El concepto no puede ir vacio")
    if datosFormulario['quantity'] == "" or float(datosFormulario['quantity']) == 0.0:  #El monto tiene que ir con int porque por defecto las entradas al formulario son str
        errores.append("El monto debe ser distinto de cero y de vacio")
    
    return errores




@app.route("/")
def index():
    dic = select_all()
    return render_template("index.html", datos = dic)


@app.route("/new", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create.html", dataForm = {})
    
    else: 
        errores = validarFormulario(request.form)
        if errores:
            return render_template("create.html", errors = errores, dataForm = request.form)
        
        else:
            insert([request.form['date'], request.form['concept'], request.form['quantity']])  #Llamo a la funcion para insertar datos
            return redirect("/")
    