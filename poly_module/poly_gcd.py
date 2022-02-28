import init

def polygcd(a, b):
    zero = init.Polynomial([0])
    if b > a:
        a, b = b, a
    while b != zero:
        a, b = b, divmod(a, b)[1]
    return a

a = init.Polynomial([1, -2, 1, 7])
b = init.Polynomial([-1, 1, 1])
print(polygcd(a * b, b))
