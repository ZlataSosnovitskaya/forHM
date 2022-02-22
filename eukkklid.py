'''
Алгорифм Евклида для целых чисел 
'''
def gcd(a,b):  # Функция gcd возвращает НОД(a,b)
    if b>a:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a



'''
Алгорифм Евклида для многочленов над полем целых чисел
'''
from numbers import Number
import itertools

class PolynomialDomainError(ValueError):
    pass 

class Polynomial:  # Определение класса многочленов, коэффиуиенты задаются списком (от свободного до старшего члена)
    def __init__(self,arg=0):
        if isinstance(arg,Number):  # Если arg - число, создаётся список из него
            self.coefficients = [arg]
        elif isinstance(arg,list):  # Если arg - уже список, он копируется
            self.coefficients = arg.copy()
        elif isinstance(arg,Polynomial): # Если arg - многочлен, список из его коэффициентов копируется
            self.coefficients = arg.coefficients.copy()
        else:  # В любом другом случае создать многочлен невозможно
            raise PolynomialDomainError("Невозможно создать многочлен из" + repr(arg))

    def __str__(self):
        return (" + ".join([
        str(c) + ("*x^" + str(i) if i > 0 else "")
        for c, i in reversed(list(zip(self.coefficients, itertools.count())))])) if len(self.coefficients) else '0'
        #  с-коэффициенты из списка, i-степени х (изменяются от степени многочлена до 0 с шагом 1)

    '''
        def __mul__(self,other):
        if isinstance (other,Number):
            other=Polynomial(other)
        sc=self.coefficients
        oc=other.coefficients
        c=[0]*(len(sc)+len(oc)-1)  # создание списка нулей длины получившегося многочлена
        if 
        for i in range(-len(c),-len(sc)):
            for n in range(0,abs(i)):
                c[i]+=sc[i+n]*oc[-n-1]
        for i in range(-len(sc),-len(oc)):
            for n in range(0,abs(i)):
                c[i]+=sc[i+n]*oc[-n-1]
        for i in range(-len(oc),0):
            for n in range(0,abs(i)):
                c[i]+=sc[i+n]*oc[-n-1]

        return Polynomial(c)
    '''
    def __sub__(self,other):

        sc=Polynomial(self)
        oc=Polynomial(other)
        ddeg=len(sc.coefficients)-len(oc.coefficients)
        d=[]

        sc.coefficients+=[0]*(len(oc.coefficients)-len(sc.coefficients))
        oc.coefficients+=[0]*(len(sc.coefficients)-len(oc.coefficients))

        return Polynomial([sce-oce for sce,oce in zip(sc.coefficients,oc.coefficients)])

    def __mul__(self,other):

        if isinstance(other, Number):
            other = Polynomial(other)
        
        c = [0] * (len(self.coefficients) + len(other.coefficients) - 1)  # создание списка нулей длины получившегося многочлена
        for sc, sci in zip(self.coefficients, itertools.count()):
            for oc, oci in zip(other.coefficients, itertools.count()):
                c[sci + oci] += sc * oc
        
        return Polynomial(c)

    '''
    def __divmod__(self,other):

        sc=Polynomial(self)
        oc=Polynomial(other)
        d=[]

        while len(sc.coefficients) >= len(oc.coefficients) > 0:
            c= sc.coefficients[-1] / oc.coefficients[-1]
            sc -= c * (oc << (len(sc.coefficients) - len(oc.coefficients)))
            d.append(c)
        
        return Polynomial(list(reversed(d))), sc        
    '''
    def __lshift__(self,deg):
        return Polynomial(([0*deg]+self.coefficients))


    def __divmod__(self,other):
        sc=Polynomial(self)
        oc=Polynomial(other)
        d=[]

        while len(sc.coefficients) >= len(oc.coefficients) > 0:
            c= sc.coefficients[-1] / oc.coefficients[-1]
            ddeg=len(sc.coefficients)-len(oc.coefficients)
            sc-=Polynomial([c])*(oc<<ddeg)
            d.append(c)
            return Polynomial(list(reversed(d))),sc
    

    def __floordiv__(self,other):
        return divmod(self,other)[0]


    def __mod__(self,other):
        return divmod(self,other)[1]


    def polygcd(self,other):
        if isinstance(other,Number):
            other=Polynomial(other)
        sc=self.coefficients
        oc=other.coefficients

        '''
        План:
        1. Сравнить, представив списки в виде десятичных чисел
        2. def gcd(a,b):  # Функция gcd возвращает НОД(a,b)
            while b!=0:
            a,b=b,a%b
            return a
        '''
        sc_float=float("0"+"".join([str(i) for i in sc]))
        oc_float=float("0"+"".join([str(i) for i in oc]))
        if oc_float>sc_float:
            sc,oc=oc,sc
        while oc!=0:
            mod=divmod(self,other)[1]
            sc,oc=oc,mod
        return sc

a=Polynomial([2,3,4,5])
b=Polynomial([5,7,6,3])
print(a.polygcd(b))
