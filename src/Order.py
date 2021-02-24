from src.Parcel import Parcel

class Order:

    def __init__(self):
        self.parcels = []

    def add(self, parcels):
        for parcel_args in parcels:
            new_parcel = Parcel(**parcel_args)
            self.parcels.append(new_parcel)

    def total_cost(self):
        return sum(map(lambda x: x.cost(), self.parcels))

    def print_parcels(self):
        for parcel in self.parcels:
            parcel.print_details()

        print(f"Total cost: ${self.total_cost()}")


