from flask import Flask

app = Flask(__name__, instance_relative_config=True)

app.config.from_object("config")  #config es el nombre del archivo config.py donde esta el secret key.

ORIGIN_DATA = "data/db_movimientos.sqlite"

from registros_ig.routes import *