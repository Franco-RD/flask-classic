from flask import Flask

app = Flask(__name__)

ORIGIN_DATA = "data/db_movimientos.sqlite"

from registros_ig.routes import *