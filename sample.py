# sample.py
from validate import Integer, validated
from logcall import logformat
from logcall import logged


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