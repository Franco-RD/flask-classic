from registros_ig import app
from flask import render_template, request, redirect  
from registros_ig.models import *

@app.route("/")
def hello():
    dic = select_all()
    return render_template("Index.html", datos = dic)