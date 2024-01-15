from registros_ig import app
from flask import render_template, request, redirect, flash  
from registros_ig.models import *
from datetime import date, datetime
from registros_ig.forms import MovementsForm


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
    ganancia = select_ingreso()
    gastos = select_egreso()
    return render_template("index.html", datos = dic, ingreso = ganancia, egreso = gastos)


@app.route("/new", methods=["GET", "POST"])
def create():
    form = MovementsForm()

    if request.method == "GET":
        return render_template("create.html", dataForm = form)
    
    else:                 
        if form.validate_on_submit():
            insert([form.date.data.isoformat(), form.concept.data, form.quantity.data])  #Llamo a la funcion para insertar datos. Hay que pasar los datos de esta manera porque si se pasa solo request.form da error.
            flash(f"Movimiento {request.form['concept']} registrado correctamente")
            return redirect("/")
        
        else:
            return render_template("create.html", dataForm = form)     


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    if request.method == "GET":
        resultado = select_by(id)
        return render_template("delete.html", data = resultado)
    
    else: 
        delete_by(id)
        flash("Movimiento borrado correctamente")
        return redirect("/")
    

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    form = MovementsForm()

    if request.method == "GET":
        resultado = select_by(id)
        #Le pasamos los datos que tenia el registro al formulario para editar
        form.date.data = datetime.strptime(resultado[1], "%Y-%m-%d")  #Hay que pasar el campo 1 a tipo fecha para que lo acepte el formulario sino da error
        form.concept.data = resultado[2]
        form.quantity.data = resultado[3]

        return render_template("update.html", dataForm = form, idForm = id)
    
    else:
        update_by(id, [form.date.data.isoformat(), form.concept.data, form.quantity.data])  #isoformat pasa la fecha a fecha en texto porque el campo de la base de datos de fecha es un text.
        flash("Movimiento actualizado correctamente")
        return redirect("/")