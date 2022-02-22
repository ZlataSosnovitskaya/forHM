'''
Матричное пространоство:
-Ввод матриц
-Матрица системы
-Прибавление к iтой строке jой строки с коэф l- T_[i,j](l)
-Паремена мест строк - S_[i,j],i!=j
-Домножение jой строки на элемент обратного класса - D_[i](E)
-Привести к ступенчатой матрице
-Метод Гаусса
-Сумма
-Произведение
-умножение матрицы на скаляр
-Транспонирование

'''
from numbers import Number
'''
Матрица m*n, n-столбцы, m-строки
'''

class MatrixError(ValueError):
    pass

class Matrix:
    def __init__(self,m,n=0):  # Ввести матрицу
        self.matrix=[]
        if isinstance(m,Number) and isinstance(n,Number):  # Ввод матрицы с консоли
            self.rows=m
            self.columns=n
            
            for i in range(self.rows):
                self.matrix.append([0]*self.columns)
                for j in range (self.columns):
                    self.matrix[i][j]=float(input('a['+str(i+1)+']['+str(j+1)+']='))

        elif isinstance(m,list) and n==0:  # Создание матрицы из созданного ранее списка
            self.rows=len(m)
            self.columns=len(m[0])
            self.comp=m
            self.matrix=m.copy()

        else:
            raise MatrixError('It is impossible to create a matrix with these parameters')

    def __str__(self):  # Выводит матрицу на экран в привычном для человека виде (таблицей)
        #for i in range(self.rows):
            #for j in range (self.rows):
                #return '\n'.join(['  '.join([str(round(s,1)) for s in self.rows]) for self.rows in self.matrix])
                return '\n'.join(['  '.join([(str(self.matrix[i][j])) for j in range(self.columns)])for i in range(self.rows)]) 
            


    def T(self,i,j,k):  # Прибавление к i-ой строке j-ой строки с коэффициентом k
        for a in range(self.columns):
            self.matrix[i-1][a]+=(self.matrix[j-1][a])*k
        return Matrix(self.matrix)
    
    def S(self,i,j):  # Перестановка строк
        for a in range(self.columns):
            self.matrix[i-1][a],self.matrix[j-1][a]=self.matrix[j-1][a],self.matrix[i-1][a]
        return Matrix(self.matrix)
    
    def stairs(self):  # Приведение к ступенчатой матрице!!!!!
        k=0
        j=0
        m=0
        for m in range(min(self.rows,self.columns)):
            for r in range(0+m,self.rows):
                b=float('0.'+"".join([str(int(abs(self.matrix[r][l]))) for l in range (m,self.columns)]))
                if b>k:
                    k=b
                    j=r+1
                self.S(1,j+1)
            for s in range(1+m,min(self.rows,self.columns)):
                self.T(s+1,m+1,-1*(self.matrix[s][m]/self.matrix[m][m]))
            
            return Matrix(self.matrix)

    def __add__(self,other):  # Cложение матриц 
        if isinstance(other,Matrix):
            if self.columns==other.columns and self.rows==other.rows:
                result=[]
                for i in range(self.rows):
                    result.append([0]*self.columns)
                    for j in range(self.columns):
                        result[i][j]=self.matrix[i][j]+other.matrix[i][j]
                return Matrix(result)

            else:
                raise MatrixError('Equal sizes of the matrix are a prerequisite for adding them together')
        else:
            raise MatrixError('You are trying to add up a matrix to'+str(type(other)))

    
    def __mul__(self,other):  
        if isinstance(other,Matrix):
            if self.columns==other.rows:
                result=[]
                for i in range(self.rows):
                    result.append([0]*other.columns)
                    for j in range(other.columns):
                        for k in range(self.columns):
                            result[i][j]+=self.matrix[i][0+k]*other.matrix[0+k][j]
                return Matrix(result)
            else:
                raise MatrixError('Self.colums and other.rows must be equel for matrix multiplication')
        
        elif isinstance(other,Number):
            for i in self.rows:
                for j in range(self.columns):
                    self.matrix[i][j]*=other
            return(Matrix(self.matrix))
        
        else:
            raise MatrixError('You are trying to multiply a matrix and a'+str(type(other)))
    
    def transpose(self):  # Транспонирование матрицы (отражение относительно диагонали)
        result=[]
        for i in range(self.columns):
            result.append([0]*self.rows)
            for j in range(self.rows):
                result[i][j]=self.matrix[j][i]
        return(Matrix(result))

    
'''
Проверка пространства матриц в действии:
'''
a=Matrix([[1,2,3],[4,5,6]])
b=Matrix([[9,8,7,5,7],[6,5,4,4,6],[2,5,7,4,5],[2,6,3,3,5]])
print(b.stairs())


