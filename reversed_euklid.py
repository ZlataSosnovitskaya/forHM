'''
Обратный алгорифм Eвклида: из gcd полуить представление безу
Ввод: a,b
Вывод: x,y,gcd, т.ч ax+by=gcd
'''
    
def egcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x,y, d = egcd(b, a % b)
        return y, x - y * (a // b), d
