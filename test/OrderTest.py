import unittest

from src.Order import Order


class OrderTest(unittest.TestCase):

    def test_order_returns_right_cost(self):
        parcels = [
            {"size": 1},
            {"size": 15}
        ]

        order = Order()
        order.add(parcels)

        assert order.total_cost() == 11

if __name__ == '__main__':
    unittest.main()
