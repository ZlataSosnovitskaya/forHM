import numpy as np
from numpy import newaxis
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

'''
Проверка
'''

N=100
SMALL = 1e-5

def test_error(solver_function):
    # Сгенерируем хорошо обусловленную систему
    while True:
        a = uniform(0.0, 1.0, (N, N))
        b = uniform(0.0, 1.0, (N,  ))

        d = det(a)
        if abs(d) <= SMALL:  # Определитель маленький — плохо
            # print(f"det: {d}")
            continue  # Попробуем ещё
        if d < 0.0:  # Отрицательный — поменяем знак
            # print(f"det: {d}")
            a = -a

        try:
            oob_solution = solve_out_of_the_box(a, b)
        except Exception as e:  # Всё-таки система плохая
            # print(f"exc: {e}")
            continue  # Попробуем ещё

        sb = a @ oob_solution
        if norm(sb - b, ord=1) > SMALL:
            # print("Bad solution...")
            continue  # Всё же не очень система получилась =)
        
        break # Всё, считаем, что мы случайно сгенерировали хорошую систему

    tested_solution = solver_function(a, b)
    return norm(tested_solution - oob_solution, ord=1)

print(test_error(gauss))
