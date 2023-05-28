from flask import Flask, render_template
from templates.functions.Cap_1.Biseccion import *
from templates.functions.Cap_1.Busqueda_Incremental import *
from templates.functions.Cap_1.Punto_Fijo import *
from templates.functions.Cap_1.Regla_Falsa import *
from templates.functions.Cap_2 import *
from templates.functions.Cap_3 import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/funciones')
def inicio_funciones():
    return render_template('inicio.html')


@app.route('/sobre_proyecto')
def sobre_proyecto():
    return render_template('sobre_proyecto.html')

@app.route("/bisection")
def bisection():
    result = Bisec('x**10-1',0,0.1,0.01)
    return render_template('biseccion.html', result=result)

@app.route("/busqincr")
def busqincr():
    result = Busqueda_Incremental('sin(x)',-7,7,0.3)
    return render_template('busqueda_incr.html', result=result)

@app.route("/pf")
def pf():
    result = MetodoPF('exp(-x)-x',0,0.01)
    return render_template('pf.html', result=result)

@app.route("/falseRule")
def falseRule():
    result = Regla_falsa('x**3+x**2+2*x+1',-1,0,0.01)
    return render_template('falseRule.html', result=result)

app.run(host='0.0.0.0', port=81, debug=True)
