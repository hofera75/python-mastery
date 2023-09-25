''' 
stock.py
'''

from structure import Structure
from validator import ValidatedFunction

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
    sell = ValidatedFunction(sell)

Stock.create_init()