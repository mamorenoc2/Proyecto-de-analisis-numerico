import numpy as np

def jacobi(A,B,mi):
    A = np.array(A,dtype=float) 
    B = np.array(B,dtype=float)
    x=[0.0]*len(B)
    count=0
    while(count<mi):
        for i in range(0,len(A)):
            sigma=0.0
            for j in range(0,len(A)):
                if(i!=j):
                    sigma = sigma + (A[i,j]*x[j])
                    x[i] = float((B[i] - sigma)/A[i,i])
        count +=1
    print("Iteraciones: ",count)
    return x

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

tam = input("ingresa el tamaño de la matriz: ")

matA = defmatrizA(tam)
matB = defmatrizB(tam)
ite = int(input("Numero De iteraciones: "))

resu=jacobi(matA,matB,ite)

print("Matriz A: ")
print(matA)
print("Matriz B")
print(matB)
print("Matriz X: ", resu)
print("Verificacion Ax=B: ", np.dot(matA,resu))