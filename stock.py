''' 
stock.py
'''

from structure import Structure, validate_attributes

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

if __name__ == 'main':
    s = Stock.from_row(['GOOG', '100', '490.1'])
