'''
Алгорифм Евклида для целых чисел 
'''
def gcd(a,b):  # Функция gcd возвращает НОД(a,b)
    if b>a:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
    