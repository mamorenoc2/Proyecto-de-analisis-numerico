import sympy as sp
x=sp.symbols('x')

def funcion(ecua='x+2'):
    global x
    return sp.sympify(ecua)

def MetodoPF(ecuacion,x_0,es):
    global x
    ecuacion=funcion(ecuacion)+x 
    ea=100
    x_r=x_0 
    iteracion=0 
    print("\nIteracion\t Xi\t\t\t\t\tError aproximado")
    print("------------------------------------------------------------------------")
    while ea>es:
        x_anterior=x_r
        x_r=ecuacion.evalf(subs={x:x_anterior})
        iteracion+=1
        if x_r !=0:
            ea=abs((x_r-x_anterior)/x_r)*100
        print(iteracion,"\t\t\t",x_r,"\t",ea)
    return x_r
#iniamos el programa con lo siguiente parametros
#a=MetodoPF('exp(-x)-x',0,0.01)

fun = input("Ingresa la funcion: ")
x0 = float(input("Ingresa X0: "))
es = float(input("Ingresa tolerancia: "))

resu=MetodoPF(fun,x0,es)

print("Raiz aproximada: ",resu)