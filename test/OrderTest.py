import unittest

from src.Order import Order


class OrderTest(unittest.TestCase):

    def test_order_returns_right_cost(self):
        parcels = [
            {"size": 1}, # cost: 3
            {"size": 15}, # cost: 8
            {"size": 101, "weight": 15} # cost: 25 + 10
        ]

        order = Order()
        order.add(parcels)

        assert order.total_cost() == 46

    def test_speedy_order_returns_right_cost(self):
        parcels = [
            {"size": 1}, # cost: 3
            {"size": 15}, # cost: 8
            {"size": 101} # cost: 2
        ]

        order = Order(speedy=True)
        order.add(parcels)

        assert order.total_cost() == 72

    def test_discount_3M(self):
        parcels = [
            {"size": 15}, # cost: 8
            {"size": 15}, # cost: 8
            {"size": 15},  # cost: 8
            {"size": 15, "weight": 4},  # cost: 10
            {"size": 15, "weight": 4},  # cost: 10
            {"size": 15, "weight": 4},  # cost: 10
        ]

        order = Order()
        order.add(parcels)

        saving = order.apply_discounts()
        assert saving == 18

    def test_discount_4S(self):
        parcels = [
            {"size": 9, "weight": 2},  # cost: 5
            {"size": 8, "weight": 3},  # cost: 7
            {"size": 7, "weight": 8},  # cost: 17
            {"size": 5, "weight": 3},  # cost: 7
        ]

        order = Order()
        order.add(parcels)

        saving = order.apply_discounts()
        assert saving == 5


    def test_discouts_mixed(self):
        parcels = [
            {"size": 9, "weight": 8},  # cost: 17
            {"size": 8, "weight": 8},  # cost: 17
            {"size": 15, "weight": 6},  # cost: 14
            {"size": 15, "weight": 6},  # cost: 14
            {"size": 7, "weight": 8},  # cost: 17
            {"size": 5},  # cost: 3
            {"size": 15},  # cost: 8
        ]
        # it's better to apply one mixt5 discount rather than 2 discount(4 small, 3 med)
        order = Order()
        order.add(parcels)

        saving = order.apply_discounts()
        assert saving == 14


if __name__ == '__main__':
    unittest.main()
