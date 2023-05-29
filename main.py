from flask import Flask, render_template, request
import numpy as np
from templates.functions.Cap_1.Biseccion import *
from templates.functions.Cap_1.Busqueda_Incremental import *
from templates.functions.Cap_1.Punto_Fijo import *
from templates.functions.Cap_1.Regla_Falsa import *
from templates.functions.Cap_1.Raices_Multiples import *
from templates.functions.Cap_1.Newton import *
from templates.functions.Cap_1.Secante import *
from templates.functions.Cap_2.Jacobi import *
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

@app.route("/pf", methods=['POST', 'GET'])
def pf():
    if request.method == 'POST':
        # Obtener los datos del formulario
        ecuacion = request.form['ecuacion']
        x_0 = float(request.form['x_0'])
        es = float(request.form['es'])
        
        result = MetodoPF(ecuacion, x_0, es)
        return render_template('pf.html', result=result)
    
    return render_template('pf.html', result=None)

@app.route("/falseRule", methods=['POST', 'GET'])
def falseRule():
    if request.method == 'POST':
        # Obtener los datos del formulario
        ecua = request.form['ecua']
        a = float(request.form['a'])
        b = float(request.form['b'])
        tolera = float(request.form['tolera'])
        
        result = Regla_falsa(ecua,a,b,tolera)
        return render_template('falseRule.html', result=result)
    
    return render_template('falseRule.html', result=None)

@app.route("/newton")
def newton():
    result = Regla_falsa('x**3+x**2+2*x+1',-1,0,0.01)
    return render_template('newton.html', result=result)

@app.route("/multipleRoots", methods=['POST', 'GET'])
def multipleRoots():
    if request.method == 'POST':
        # Obtener los datos del formulario
        ecuacion = request.form['ecuacion']
        x0 = float(request.form['x0'])
        tolerancia = float(request.form['tolerancia'])
        iteraciones = float(request.form['iteraciones'])
        
        result = Raices_Multiples(ecuacion,x0,tolerancia,iteraciones)
        return render_template('multipleRoots.html', result=result)
    
    return render_template('multipleRoots.html', result=None)

@app.route("/secant", methods=['POST', 'GET'])
def secant():
    if request.method == 'POST':
        # Obtener los datos del formulario
        fx = request.form['fx']
        a = float(request.form['a'])
        b = float(request.form['b'])
        tolera = float(request.form['tolera'])
        iteraciones = float(request.form['iteraciones'])
        
        result = secante(fx,a,b,tolera,iteraciones)
        return render_template('secant.html', result=result)
    
    return render_template('secant.html', result=None)

@app.route("/jacobi" , methods=['POST', 'GET'])
def jacobi():
    if request.method == 'POST':
        tam = int(request.form['tam'])
        matA = [[float(request.form[f'matA_{i}_{j}']) for j in range(tam)] for i in range(tam)]
        matB = [[float(request.form[f'matB_{i}'])] for i in range(tam)]
        ite = int(request.form['ite'])
        
        result = jacobi(matA, matB, ite)
        return render_template('jacobi.html', tam=tam, matA=matA, matB=matB, result=result)
    
app.run(host='0.0.0.0', port=81, debug=True)
