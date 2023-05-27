import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


# PROCEDIMIENTO
def vandermonde(xi,fi): 
    muestras = 101 # muestras = tramos+1
    xi = np.array(xi)
    B = np.array(fi)
    n = len(xi)

    # Matriz Vandermonde D
    D = np.zeros(shape=(n,n),dtype =float)
    for i in range(0,n,1):
        for j in range(0,n,1):
            potencia = (n-1)-j # Derecha a izquierda
            D[i,j] = xi[i]**potencia

    # Aplicar métodos Unidad03. Tarea
    # Resuelve sistema de ecuaciones A.X=B
    coeficiente = np.linalg.solve(D,B)

    # Polinomio en forma simbólica
    x = sym.Symbol('x')
    polinomio = 0
    for i in range(0,n,1):
        potencia = (n-1)-i   # Derecha a izquierda
        termino = coeficiente[i]*(x**potencia)
        polinomio = polinomio + termino

    # Polinomio a forma Lambda
    # para evaluación con vectores de datos xin
    px = sym.lambdify(x,polinomio)

    # Para graficar el polinomio en [a,b]
    a = np.min(xi)
    b = np.max(xi)
    xin = np.linspace(a,b,muestras)
    yin = px(xin)
    return D, coeficiente,polinomio, xin, yin

# INGRESO
#xi = [1,2,4.5]
#fi = [2.5,5,6.7]   

def defmatriz(n):
    '''n = int(input("ingrese filas"))
    m = int(input("ingrese columnas"))'''
    #a = n*m
    matriz = []
    n = int(n)
    #val = float(input("ingrese dato: "))
    matriz = [float(input("ingrese dato: ")) for i in range(n)] 

    #print(matriz)
    return matriz

tam = input("ingresa el tamaño de los arreglos: ")

print("Ingrese los datos de Xi: ")
xi = defmatriz(tam)
print("Ingrese los datos Yi: ")
fi = defmatriz(tam)

(D,coeficiente,polinomio, xin, yin)=vandermonde(xi,fi)
# SALIDA
print('Matriz Vandermonde: ')
print(D)
print('los coeficientes del polinomio: ')
print(coeficiente)
print('Polinomio de interpolación: ')
print(polinomio)

# Grafica
plt.plot(xi,fi,'o', label='[xi,fi]')
plt.plot(xin,yin, label='p(x)')
plt.xlabel('xi')
plt.ylabel('fi')
plt.legend()
plt.title("Vandermonde")
plt.show()