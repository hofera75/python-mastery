import unittest
from pyreview.stock import Stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_create_keywords(self):
        s = Stock(name='GOOG',shares=100,price=490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = Stock(name='GOOG',shares=100,price=490.1)
        c = s.cost
        self.assertEquals(c, 100*490.1)

    def test_sell(self):
        s = Stock(name='GOOG',shares=100,price=490.1)
        s.sell(10)
        self.assertEquals(s.shares, 90)

    def test_from_row(self):
        s = Stock.from_row(('MSFT',200,51.23))
        self.assertEqual(s.name, 'MSFT')
        self.assertEqual(s.shares, 200)
        self.assertEqual(s.price, 51.23)

    def test_repr(self):
        s = Stock(name='GOOG',shares=100,price=490.1)
        self.assertEquals(s.__repr__(),"Stock('GOOG',100,490.1)")

    def test_eq(self):
        s1 = Stock(name='GOOG',shares=100,price=490.1)
        s2 = Stock(name='GOOG',shares=100,price=490.1)
        self.assertTrue(s1.__eq__(s2))

    def test_bad_shares(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
             s.shares = '50'

    def test_bad_negative_shares(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
             s.shares = -50

    def test_bad_price(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
             s.price = '50'

    def test_bad_negative_price(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
             s.price = -50.0

    def test_bad_attribute(self):
        s = Stock('GOOG', 100, 490.1)
        with self.assertRaises(AttributeError):
             s.share = 50
    

if __name__ == '__main__':
    unittest.main()