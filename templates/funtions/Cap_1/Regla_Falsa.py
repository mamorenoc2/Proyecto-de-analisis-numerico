import sympy as sp
import numpy as np

x=sp.symbols('x')

def funcion(func):
    global x
    return sp.sympify(func)

def Regla_falsa(ecua,a,b,tolera):
    global x
    ecuacion=funcion(ecua)
    tramo = abs(b-a)
    fa = ecuacion.evalf(subs={x:a})
    fb = ecuacion.evalf(subs={x:b})
    while not(tramo<=tolera):
        c = b - fb*(a-b)/(fa-fb)
        fc = ecuacion.evalf(subs={x:c})
        cambio = np.sign(fa)*np.sign(fc)
        if cambio>0:
            tramo = abs(c-a)
            a = c
            fa = fc
        else:
            tramo = abs(b-c)
            b = c
            fb = fc

    return c, tramo

fun = input("Ingresa la funcion: ")
a = float(input("Ingresa intervalo a: "))
b = float(input("Ingresa intervalo b: "))
tol = float(input("Ingresa la tolerancia: "))

#(c,tramo)=Regla_falsa('x**3+x**2+2*x+1',-1,0,0.01)
(Raiz,Error)=Regla_falsa(fun,a,b,tol)

# SALIDA
print("")
print('raiz:  ',Raiz)
print('error: ',Error)