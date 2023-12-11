class calculator:
    """
    >>> calc = calculator(6, 4)
    >>> calc.add()
    10
    >>> calc.mult()
    24
    >>> calc.div() 
    1.5
    >>> calc.sub() 
    2
    """

    def __init__(self, a, b):
        self.a=a
        self.b=b

    def add(self):
        return self.a + self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b

if __name__ == "__main__":
    import doctest
    doctest.testmod()