# sample.py
from structly.validate import Integer, validated
from metaprogramming.logcall import logformat
from metaprogramming.logcall import logged
from metaprogramming.enforcer import enforce


@logged
def add(x,y):
    return x+y

@logged
def sub(x,y):
    return x-y

@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y:Integer) -> Integer:
    return x ** y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x,y):
    return x*y

@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y