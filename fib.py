import itertools
class Fib:
    class _Fib_iter:
        def __init__(self):
            self.fib1 = 0
            self.fib2 = 0
            self.fib3 = 1
            self.i = 1
        def __next__(self):
            f = self.fib3
            self.i += 1
            self.fib1 = self.fib2
            self.fib2 = self.fib3
            self.fib3 = self.fib1 + self.fib2
            return f
    def __iter__(self):
        return Fib._Fib_iter()

f = Fib()
print(list(itertools.islice(Fib(), 27)))
