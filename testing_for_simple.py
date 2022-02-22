'''
Функция должна проверять число на простоту
Если число простое - True
Если число составное - False
'''

import math

def check_prime(a):
    answer = True
    b = 2
    while b <= round(math.sqrt(a)):
        if a % (b) == 0:
            answer = False
            break
        b += 1
    return answer    

a = int(input("Введите число: "))    
print(check_prime(a))