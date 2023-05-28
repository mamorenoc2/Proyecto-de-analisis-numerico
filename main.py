from flask import Flask, render_template, request
from templates.functions.Cap_1.Biseccion import *
from templates.functions.Cap_1.Busqueda_Incremental import *
from templates.functions.Cap_1.Punto_Fijo import *
from templates.functions.Cap_1.Regla_Falsa import *
from templates.functions.Cap_1.Raices_Multiples import *
from templates.functions.Cap_1.Newton import *
from templates.functions.Cap_1.Secante import *
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

@app.route("/bisection", methods=['POST', 'GET'])
def bisection():
    if request.method == 'POST':
        # Obtener los datos del formulario
        func = request.form['func']
        xl = float(request.form['xl'])
        xu = float(request.form['xu'])
        es = float(request.form['es'])
        result = Bisec(func, xl, xu, es)
        print(result)
        
        return render_template('biseccion.html', result=result)
    
    return render_template('biseccion.html', result=None)

@app.route("/busqincr", methods=['POST', 'GET'])
def busqincr():
    if request.method == 'POST':
        # Obtener los datos del formulario
        ecuacion = request.form['func']
        a = float(request.form['xl'])
        b = float(request.form['xu'])
        deltaX = float(request.form['es'])
        result = Busqueda_Incremental(ecuacion, a, b, deltaX)
        return render_template('busqueda_incr.html', result=result)
        
    return render_template('busqueda_incr.html', result=None)

@app.route("/pf")
def pf():
    result = MetodoPF('exp(-x)-x',0,0.01)
    return render_template('pf.html', result=result)

@app.route("/falseRule")
def falseRule():
    result = Regla_falsa('x**3+x**2+2*x+1',-1,0,0.01)
    return render_template('falseRule.html', result=result)

@app.route("/newton")
def newton():
    result = Regla_falsa('x**3+x**2+2*x+1',-1,0,0.01)
    return render_template('newton.html', result=result)

@app.route("/multipleRoots")
def multipleRoots():
    result = Raices_Multiples('x**3+x**2+2*x+1',5,0.01,100)
    return render_template('multipleRoots.html', result=result)

@app.route("/secant")
def secant():
    result = secante('x**3+x**2+2*x+1',-1,0,0.001,100)
    return render_template('secant.html', result=result)

app.run(host='0.0.0.0', port=81, debug=True)
