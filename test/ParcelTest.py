import unittest

from src.Parcel import Parcel


class MyTestCase(unittest.TestCase):

    def test_size_parcel_cost(self):

        small_parcel = Parcel(size=5)
        assert small_parcel.cost() == 3

        medium_parcel = Parcel(size=25)
        assert medium_parcel.cost() == 8

        large_parcel = Parcel(size=57)
        assert large_parcel.cost() == 15

        xl_parcel = Parcel(size=1234)
        assert xl_parcel.cost() == 25



if __name__ == '__main__':
    unittest.main()
