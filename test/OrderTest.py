import unittest

from src.Order import Order


class OrderTest(unittest.TestCase):

    def test_order_returns_right_cost(self):
        parcels = [
            {"size": 1}, # cost: 3
            {"size": 15}, # cost: 8
            {"size": 101} # cost: 25
        ]

        order = Order()
        order.add(parcels)

        assert order.total_cost() == 36

    def test_speedy_order_returns_right_cost(self):
        parcels = [
            {"size": 1}, # cost: 3
            {"size": 15}, # cost: 8
            {"size": 101} # cost: 2
        ]

        order = Order(speedy=True)
        order.add(parcels)

        assert order.total_cost() == 72


if __name__ == '__main__':
    unittest.main()
