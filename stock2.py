''' 
stock.py
'''

import csv

import validator

class Stock:
    '''
    Stock
    '''
    __slots__ = ['name', '_shares', '_price']
    _types = (str, int , float)

    def __init__(self, name, shares, price):
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
        validator.PositiveInteger.check(value)
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        validator.PositiveFloat.check(value)
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
