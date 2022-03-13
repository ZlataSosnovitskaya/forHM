from numbers import Number
import itertools


class PolynomialDomainError(ValueError):
    pass


class PolynomialTypeError(TypeError):
    pass


class Polynomial:
    """Многочлен над полем (пока числовым, а там видно будет)"""

    def __init__(self, arg=0)->list:
        """
        coefficients -- коэффициенты
        """
        if isinstance(arg, Number):
            self.coefficients = [arg]
        elif isinstance(arg, list):
            self.coefficients = arg.copy()
        elif isinstance(arg, Polynomial):
            self.coefficients = arg.coefficients.copy()
        else:
            raise PolynomialTypeError("You are trying to create polynomial from " + repr(arg))

        self.cleanup(self.coefficients)

    @staticmethod
    def cleanup(coefficients) -> list:
        """
        Удаление старших коэффициентов, если они близки к 0, для понижения степени
        """
        epsilon = 1e-25
        while len(coefficients) and abs(coefficients[-1]) < epsilon:
            del coefficients[-1]

    def __str__(self) -> str:
        return (" + ".join([
            str(c) + ("*x^" + str(i) if i > 0 else "")
            for c, i in reversed(list(zip(self.coefficients, itertools.count())))
        ])) if len(self.coefficients) else '0'

    def __eq__(self, other):
        """Вот тут точно полезно почитать https://wiki.python.org/moin/MultipleDispatch..."""
        if isinstance(other, Number):
            other = Polynomial(other)

        if isinstance(other, Polynomial):
            return self.coefficients == other.coefficients
        else:
            raise PolynomialDomainError("Can't say if Polynomial is equal to " + str(type(other)))

    def __lshift__(self, deg) ->list:
        return Polynomial(([0] * deg) + self.coefficients)

    def __add__(self, other) ->list:
        if isinstance(other, Number):
            other = Polynomial(other)

        sc = self.coefficients.copy()
        oc = other.coefficients.copy()

        # make lengths equal
        sc += [0] * (len(oc) - len(sc))
        oc += [0] * (len(sc) - len(oc))

        return Polynomial([
            sce + oce for sce, oce in zip(sc, oc)
        ])

    def __radd__(self, other) ->list:
        return self.__add__(other)  # Коммутативность

    def __neg__(self) ->list:
        return Polynomial([-c for c in self.coefficients])

    def __sub__(self, other)->list:
        if isinstance(other, Number):
            other = Polynomial(other)

        return self.__add__(other.__neg__())

    def __rsub__(self, other) ->list:
        return self.__neg__().__add__(other)

    def __mul__(self, other) ->list:
        if isinstance(other, Number):
            other = Polynomial(other)

        c = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for sc, sci in zip(self.coefficients, itertools.count()):
            for oc, oci in zip(other.coefficients, itertools.count()):
                c[sci + oci] += sc * oc

        return Polynomial(c)

    def __rmul__(self, other)->list:
        return self.__mul__(other)  # Коммутативность

    def __divmod__(self, other)->list:
        if isinstance(other, Number):
            other = Polynomial(other)

        sc = Polynomial(self)
        oc = other
        d = []

        while len(sc.coefficients) >= len(oc.coefficients) > 0:
            c = sc.coefficients[-1] / oc.coefficients[-1]
            sc -= c * (oc << (len(sc.coefficients) - len(oc.coefficients)))
            d.append(c)
        return Polynomial(list(reversed(d))), sc

    def __floordiv__(self, other)->list:
        return divmod(self, other)[0]

    def __mod__(self, other)->list:
        return divmod(self, other)[1]

    def __rfloordiv__(self, other)->list:
        return divmod(other, self)[0]

    def __rmod__(self, other)->list:
        return divmod(other, self)[1]

    def __rdivmod__(self, other)->list:
        return Polynomial(other).__divmod__(self)

    def __complex__(self)->list:
        """Преобразование к комплексному числу, complex(...)"""
        if not len(self.coefficients):
            return 0j
        elif len(self.coefficients) == 1:
            return complex(self.coefficients[0])
        else:
            raise PolynomialDomainError("Can't consider higher degree polynomial as a complex")

    def __float__(self)->list:
        """Преобразование к комплексному числу, complex(...)"""
        if not len(self.coefficients):
            return 0.0
        elif len(self.coefficients) == 1:
            return float(self.coefficients[0])
        else:
            raise PolynomialDomainError("Can't consider higher degree polynomial as a float")

    def __int__(self) -> int:
        if not len(self.coefficients):
            return 0
        elif len(self.coefficients) == 1:
            return int(self.coefficients[0])
        else:
            raise PolynomialDomainError("Can't consider higher degree polynomial as an integer")

    def __gt__(self, other):
            if isinstance(other, Number):
                other = Polynomial(other)
            sc = self.coefficients.copy()
            oc = other.coefficients.copy()
            if len(sc) - 1 > len(oc) - 1:
                return True
            else:
                return False