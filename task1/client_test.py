import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        expected = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_ask']['price'] + quote['top_bid']['price'])/2)
        self.assertEqual (getDataPoint(quote), expected)
   
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        expected = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_ask']['price'] + quote['top_bid']['price'])/2)
        self.assertEqual (getDataPoint(quote), expected)

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_normalRatio(self):
    price_a = [0,1,2,3]
    price_b = [3,2,1,1]
    expected = [0,0.5, 2, 3]
    for i in range(len(price_a)):
      self.assertEqual (getRatio(price_a[i], price_b[i]), expected[i])
  
  def test_getRatio_zeroDivision(self):
    price_a = [0,1,2,99.9]
    price_b = [0,0,0,0]
    # getRatio should return None for all divisions by zero
    expected = [None, None, None, None]
    for i in range(len(price_a)):
      self.assertIsNone (getRatio(price_a[i], price_b[i]))





if __name__ == '__main__':
    unittest.main()
