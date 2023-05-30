import numpy as np
import sympy as sp
import pandas as pd

x=sp.symbols('x')

def jacobi_m(A,B,mi):
    A = np.array(A,dtype=float)
    B = np.array(B,dtype=float)
    x=[0.0]*len(A)
    count=0
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    T = np.linalg.inv(D - L) @ (D + U)
    m_itera=np.array([]) 
    m_x=np.array([])   
    while(count<mi):
        m_itera=np.append(m_itera,count)
        m_x=np.append(m_x,x)
        for i in range(0,len(A)):
            sigma=0.0
            for j in range(0,len(A)):
                if(i!=j):
                    sigma = sigma + (A[i,j]*x[j])
                    x[i] = float((B[i] - sigma)/A[i,i])
        count +=1

    itera=pd.Series(m_itera,name="Iteration")
    Xi = pd.Series(m_x, name="")

    tabla=pd.concat([itera,Xi],axis=1)
    #print("Iteraciones: ",count)
    return x, tabla

def matJacobiSeid(x0,A,b,Tol,niter,met):
    c=0
    error=Tol+1
    A = np.array(A,dtype=float)
    b = np.array(b,dtype=float)
    x0 = np.array(x0,dtype=float)
    D=np.diag(np.diag(A))
    L=-np.tril(A, -1)
    U=-np.triu(A, 1)
    E=np.array([])
    m_itera=np.array([]) 
    m_x=np.array([])  
    while error>Tol and c<niter:
        if met == 0:
            T = np.linalg.inv(D) @ (L + U)
            C = np.linalg.inv(D) @ b
            x1 = (T @ x0) + C
        if met == 1:
            T=np.linalg.inv(D-L) @ (U)
            C=np.linalg.inv(D-L) @ b
            x1=(T @ x0) + C
        E = np.append(E,np.linalg.norm(x1-x0, np.inf))
        m_itera=np.append(m_itera,c)
        m_x=np.append(m_x,str(x1).replace("\n", ""))
        error=np.linalg.norm(x1-x0, np.inf)
        x0=x1
        c=c+1
    if error < Tol:
        s=x0
        n=c
    else: 
        s=x0
        n=c 
    itera=pd.Series(m_itera,name="Iteration")
    err=pd.Series(E,name="Error")
    Xi = pd.Series(m_x, name="")

    tabla=pd.concat([itera,err,Xi],axis=1)

    return pd.DataFrame(s), tabla

#A= [[8,-3,2],[4,11,-1],[6,3,12]]
#B= [[20],[33],[36]]

def defmatrizA(n):
    '''n = int(input("ingrese filas"))
    m = int(input("ingrese columnas"))'''
    #a = n*m
    matriz = []
    n = int(n)

    for i in range(n):
        matriz.append([])
        for j in range(n):
            val = float(input("ingrese dato: "))
            matriz[i].append(val)

    #print(matriz)
    return matriz

def defmatrizB(n):
    '''n = int(input("ingrese filas"))
    m = int(input("ingrese columnas"))'''
    #a = n*m
    matriz = []
    n = int(n)
    
    print("Ingrese los datos de la matriz B: ")
    for i in range(n):
        matriz.append([])
        for j in range(1):
            val = float(input("ingrese dato: "))
            matriz[i].append(val)

    #print(matriz)
    return matriz

# tam = input("ingresa el tamaño de la matriz: ")

# matA = defmatrizA(tam)
# matB = defmatrizB(tam)
# ite = int(input("Numero De iteraciones: "))

# resu=jacobi(matA,matB,ite)

# print("Matriz A: ")
# print(matA)
# print("Matriz B")
# print(matB)
# print("Matriz X: ", resu)
# print("Verificacion Ax=B: ", np.dot(matA,resu))