
"""

Built-in Data Types and Custom Data Types

1 + 2.2     =>  3.2
2.2 + 1     =>  3.2

1kg + 2.2lb =>  2kg
2.2lb + 1kg =>  4.4lb

1$ + 5000kyats  => 2$
5000kyats + 1$  => 10000kyats

#################################################

Custom Data Types

class     -   Dollar
data      -   n
method    -   add(self, other)

#################################################

Step.1 (Draw dollar Type)


class Dollar:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        return self.n + other.n


x = Dollar(1)
print(x)

#################################################

Step.2 (repr) (1$)

<__main__.Dollar object at 0x1027d9520>   --->    1$


class Dollar:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        return self.n + other.n

    def __repr__(self):
        return f"{self.n}$"


x = Dollar(1)
print(x)

#################################################

Step.3 (+) (__add__)


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

    def __repr__(self):
        return f"{self.n}$"


x = Dollar(1)
y = Dollar(2)

z = x + y      # x.__add__(y)

print(z)

#################################################

Step.4 ( result of addition => 3$ )

>> Dollar(self.n + other.n)


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Dollar(self.n + other.n)

    def __repr__(self):
        return f"{self.n}$"


x = Dollar(1)
y = Dollar(2)

z = x + y

print(z)

#################################################

Step.5 ( Draw Kyat )

class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Dollar(self.n + other.n)

    def __repr__(self):
        return f"{self.n} $"


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Kyat(self.n + other.n)

    def __repr__(self):
        return f"{self.n} kyat"


x = Dollar(1)
y = Kyat(5000)

#################################################

1 $ + 5000 kyats  => 5001 $
5000 kyats + 1 $  => 5001 kyat

#################################################

Step.6  (2 $, 10000 kyat)

1 $ + 5000 kyats  => 2 $
5000 kyats + 1 $  => 10000 kyat


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n + other.n)

        if type(other) is Kyat:
            return Dollar(self.n + other.n / 5000)

    def __repr__(self):
        return f"{self.n} $"


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n + other.n)

        if type(other) is Dollar:
            return Kyat(self.n + other.n * 5000)

    def __repr__(self):
        return f"{self.n} kyat"


x = Dollar(1)
y = Kyat(5000)

print(x + y)
print(y + x)

#################################################

Step.7  ( - ) ( __sub__ )


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n + other.n)

        if type(other) is Kyat:
            return Dollar(self.n + other.n / 5000)

    def __sub__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n - other.n)

        if type(other) is Kyat:
            return Dollar(self.n - other.n / 5000)

    def __repr__(self):
        return f"{self.n} $"


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n + other.n)

        if type(other) is Dollar:
            return Kyat(self.n + other.n * 5000)

    def __sub__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n - other.n)

        if type(other) is Dollar:
            return Kyat(self.n - other.n * 5000)

    def __repr__(self):
        return f"{self.n} kyat"


x = Dollar(2)
y = Kyat(5000)

print(x - y)
print(y - x)

#################################################

Step.8  (literal)

int(1)         =>   1
str("a")       =>   "a", 'a'
Dollar(1)      =>   1 dollar
Kyat(5000)     =>   5000 kyat

#################################################

print(1 + 2)
print(int(1).__add__(int(2)))

print(5000 .kyat + 10000 .kyat)
print(Kyat(5000).__add__(Kyat(10000)))

#################################################

from custom_literals import literal

@literal(int, float, name="kyat")
def f2(n):
    return Kyat(n)

#################################################


from custom_literals import literal


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n + other.n)

        if type(other) is Kyat:
            return Dollar(self.n + other.n / 5000)

    def __sub__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n - other.n)

        if type(other) is Kyat:
            return Dollar(self.n - other.n / 5000)

    def __repr__(self):
        return f"{self.n} $"


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n + other.n)

        if type(other) is Dollar:
            return Kyat(self.n + other.n * 5000)

    def __sub__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n - other.n)

        if type(other) is Dollar:
            return Kyat(self.n - other.n * 5000)

    def __repr__(self):
        return f"{self.n} kyat"


@literal(int, float, name="dollar")
def f1(n):
    return Dollar(n)


@literal(int, float, name="kyat")
def f2(n):
    return Kyat(n)


print(5000 .kyat + 1 .dollar)
print(1 .dollar + 5000 .kyat)


#################################################

Step.9  (equal to ) ( == ) ( __eq__ )

def __eq__(self, other):
    return self.n == other.n
    
#################################################
    
Step.10  (1 dollar == 5000 kyat) (5000 kyat == 1 dollar)
    
def __eq__(self, other):
    if type(other) is Dollar:
        return self.n == other.n
    if type(other) is Kyat:
        return self.n == other.n / 5000
        
        
def __eq__(self, other):
    if type(other) is Kyat:
        return self.n == other.n
    if type(other) is Dollar:
        return self.n == other.n * 5000        
        

#################################################

from custom_literals import literal


class Dollar:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n + other.n)

        if type(other) is Kyat:
            return Dollar(self.n + other.n / 5000)

    def __sub__(self, other):
        if type(other) is Dollar:
            return Dollar(self.n - other.n)

        if type(other) is Kyat:
            return Dollar(self.n - other.n / 5000)

    def __repr__(self):
        return f"{self.n} $"

    def __eq__(self, other):
        if type(other) is Dollar:
            return self.n == other.n
        if type(other) is Kyat:
            return self.n == other.n / 5000


class Kyat:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n + other.n)

        if type(other) is Dollar:
            return Kyat(self.n + other.n * 5000)

    def __sub__(self, other):
        if type(other) is Kyat:
            return Kyat(self.n - other.n)

        if type(other) is Dollar:
            return Kyat(self.n - other.n * 5000)

    def __repr__(self):
        return f"{self.n} kyat"

    def __eq__(self, other):
        if type(other) is Kyat:
            return self.n == other.n
        if type(other) is Dollar:
            return self.n == other.n * 5000


@literal(int, float, name="dollar")
def f1(n):
    return Dollar(n)


@literal(int, float, name="kyat")
def f2(n):
    return Kyat(n)


x = Dollar(1)
y = Kyat(5000)

print(x == y)
print(y == x)

print(3 .dollar == 15000 .kyat)

##################################################################################################
    

"""
