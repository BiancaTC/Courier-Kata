from src.Parcel import Parcel

class Order:

    def __init__(self, speedy=False):
        self.parcels = []
        self.speedy = speedy

    def add(self, parcels):
        for parcel_args in parcels:
            new_parcel = Parcel(**parcel_args)
            self.parcels.append(new_parcel)

    def total_cost(self):
        parcel_cost = sum(map(lambda x: x.cost(), self.parcels))
        parcel_cost = 2 * parcel_cost if self.speedy else parcel_cost
        return parcel_cost

    def print_parcels(self):
        for parcel in self.parcels:
            parcel.print_details()

        parcels_cost = self.total_cost()
        if self.speedy:
            print(f"Speedy order: ${parcels_cost/2}")

        print(f"Total cost: ${parcels_cost}")


