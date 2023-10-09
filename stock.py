''' 
stock.py
'''

from structly import *
from structly.validate import PositiveInteger, PositiveFloat
from typedproperty import String

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

if __name__ == '__main__':
    print("Test")
    portfolio = read_csv_as_instances('Data/portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
