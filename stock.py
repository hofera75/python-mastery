''' 
stock.py
'''

from structure import Structure
from validate import validated

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares):
        self.shares -= nshares

Stock.create_init()