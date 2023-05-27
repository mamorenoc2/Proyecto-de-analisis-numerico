import sympy as sp


x=sp.symbols('x')

def funcion(ecua):
    global x
    return sp.sympify(ecua)

def MetodoPF(ecuacion,x_0,es,maxIte):
    global x
    ecuacion=funcion(ecuacion)
    derivada=sp.diff(ecuacion)
    f_NR=x-(ecuacion/derivada)#formula de Newton Rhapson
    ea=100 #error aproximado 100%
    x_r=x_0 #x_i+1
    interaciones=0
    print("\nIteracion\t Xi\t\t\tError aproximado")
    print("------------------------------------------------------------------------")
    while ea>es:
        x_anterior=x_r# x_anterior = x_i
        x_r=f_NR.evalf(subs={x:x_anterior})
        if x_r !=0:
            ea=abs((x_r-x_anterior)/x_r)*100
        interaciones=interaciones+1
        print(interaciones,"\t\t",x_r,"\t",ea)
        if interaciones>=maxIte:
            print("\nEl metodo no converge\n")
            break
    return x_r
#iniamos el programa con lo siguiente parametros
ecua=input("Ecuacion: ")
x_0=float(input("X0: "))
tolerancia=float(input("Tolerancia: "))
maxItera=int(input("Iteraciones: "))
a=MetodoPF(ecua,x_0,tolerancia,maxItera)
print("\nRaiz aproximada: ",a)