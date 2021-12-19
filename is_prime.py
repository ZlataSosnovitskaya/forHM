"""
Реализация проверки числа на простоту
"""

import unittest
from sympy.ntheory import primefactors
import math

def is_prime(num):
    answer = True
    b = 2
    while b <= round(math.sqrt(num)):
        if num % (b) == 0:
            answer = False
            break
        b += 1
    return answer

print(is_prime(4))  #False, число 4 - составное
print(primefactors(4))
print(len(primefactors(4))<=1)  # True --- так как у 4 - один делитель


class PrimeCheckTest(unittest.TestCase):
    """Тесты для функции проверки на простоту"""

    def setUp(self):
        """Инициализация"""
        pass

    @staticmethod
    def is_exatly_prime(num):
        """
        Точная проверка того, простое ли (True) или составное (False) число
        """
        return len(primefactors(num)) <=1

    def test_return_type(self):
        """Проверка того, что функция возвращает bool"""
        for i in range(10):
            self.assertIsInstance(
                is_prime(i), bool,
                msg="Функция должна возвращать bool"
            )

    def test_first_1000(self):
        """Проверка 0..999"""
        for i in range(1000):
            self.assertEqual(
                is_prime(i), PrimeCheckTest.is_exatly_prime(i),
                msg=f"Функция наврала на {i}"
            )

    def test_carmichael(self):
        """Проверка на числах Кармайкла"""
        # можно было sympy.functions.combinatorial.numbers.carmichael,
        # но очень не быстро, лучше взять готовые https://oeis.org/A002997
        carmichaels = [
            561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341,
            41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217,
            162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153,
            340561, 399001, 410041, 449065, 488881, 512461
        ]

        for _ in range(10000):
            for c in carmichaels:
                self.assertFalse(
                    is_prime(c),
                    msg=f"Функция наврала на числе Кармайкла {c}"
                )

    def test_trivial_pseudorandoms(self):
        """
        Проверка на тривиальных псевдослучайных
        Генерация линейным конгруэнтным генератором
        https://en.wikipedia.org/wiki/Linear_congruential_generator#Parameters_in_common_use 
        """
        a = 6364136223846793005
        s = 1
        c = 1
        for _ in range(1000):
            s = (s * a + c) % (1 << 64)
            r = s >> 32  # старшие 32 бита
            self.assertEqual(
                is_prime(r), PrimeCheckTest.is_exatly_prime(r),
                msg=f"Функция наврала на {r}"
            )

if __name__ == '__main__':
    unittest.main()