import poly_module as pm

def polygcd(a, b):
    zero = pm.Polynomial([0])
    if b > a:
        a, b = b, a
    while b != zero:
        a, b = b, divmod(a, b)[1]
    return a

a = pm.Polynomial([1, -2, 1, 7])
b = pm.Polynomial([-1, 1, 1])
print(polygcd(a * b, b))
