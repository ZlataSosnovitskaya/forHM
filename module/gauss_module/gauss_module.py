import numpy as np
from numpy import newaxis
from numpy import array
from numpy.linalg import solve as solve_out_of_the_box
from numpy.linalg import norm, det
from numpy.random import uniform


def gauss(a, b):

    a = a.copy()
    b = b.copy()
    c=np.hstack((a,b[:, newaxis]))  # создадим расширенную матрицу системы
    
    def forward():  # Прямой ход - приход к верхнетругольной матрице
        for i in range(len(a)-1):
            for j in range(i,len(a)-1):
                c[j+1]-=c[i]*c[j+1][i]/c[i][i]
   
    def backward():  # Обратный ход - нахождение всех, от n до 1
        n=len(c)
        x = np.zeros(len(b), dtype=float)
        for i in range(n):
            sum=c[n-i-1][n]
            for j in range(i):
                sum-=c[n-i-1][n-j-1]*x[n-j-1]
            x[n-i-1]=sum/c[n-i-1][n-i-1]
        return x

    forward()
    x=backward()
    return x