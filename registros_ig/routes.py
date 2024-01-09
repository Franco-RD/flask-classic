from registros_ig import app
from flask import render_template, request, redirect  

@app.route("/")
def hello():
    return "Hola esto es flask"