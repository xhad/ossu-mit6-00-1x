def a(x):
   '''
   x: int or float.
   '''
   return x + 1


def b(x):
    return x + 1.0

def c(x, y):
    return x + y

def d(x, y):
    return x > y

def e(x, y, z) :
    return x >= y and x >=z

def f(x, y):
    return x + y - 2

print (a(6))
print (a(-5.3))
print (a(a(a(6))))
print (c(a(1), b(1)))
print (d('apple', 11.1))
print (e(a(3), b(4), c(3, 4)))
print (f)
