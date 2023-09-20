''' 
stock.py
'''

import csv
from typing import Any
from validator import String, PositiveInteger, PositiveFloat
import typedproperty

class Stock:
    '''
    Stock
    '''
    _types = (str, int , float)

    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        '''
        from row
        '''
        values = [func(value) for func, value in zip(cls._types, row)]
        return cls(*values)

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError
        if value < 0:
            raise ValueError
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError
        if value < 0:
            raise ValueError
        self._price = value

    @property
    def cost(self):
        '''
        cost
        '''
        return self.shares * self.price

    def sell(self, shares):
        '''
        sell
        '''
        if shares > self.shares:
            raise ValueError("Cannot sell more shares than owned.")
        self.shares -= shares


    def __setattr__(self, name, value):
        if name not in { 'name', 'shares', '_shares', 'price', '_price' }:
            raise AttributeError('No attribute %s' % name)
        super().__setattr__(name, value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.shares!r}, {self.price!r})"
    
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == 
                                             (other.name, other.shares, other.price))


# A function that reads a file into a list of dicts
def read_portfolio(cls, filename):
    '''
    read
    '''
    result = []
    with open(filename, encoding='utf') as file:
        rows = csv.reader(file)
        _ = next(rows) # headers
        for row in rows:
            stock = cls.from_row(row)
            result.append(stock)
    return result

def print_portfolio(pofo):
    '''
    print
    '''
    print('%10s %10s %10s' % ('name','shares', 'price'))
    print('---------- ---------- ----------')
    for s in pofo:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

if __name__ == '__main__':
    portfolio = read_portfolio(Stock, 'Data/portfolio.csv')
    print_portfolio(portfolio)
