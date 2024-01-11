from registros_ig import app
from flask import render_template, request, redirect  
from registros_ig.models import *

@app.route("/")
def index():
    dic = select_all()
    return render_template("Index.html", datos = dic)

@app.route("/new")
def create():

    return "esto es una vista de registro"