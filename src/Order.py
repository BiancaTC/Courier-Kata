import copy

from src.Parcel import Parcel

class Order:

    def __init__(self, speedy=False):
        self.parcels = []
        self.speedy = speedy

    def add(self, parcels):
        for parcel_args in parcels:
            new_parcel = Parcel(**parcel_args)
            self.parcels.append(new_parcel)


    def apply_discounts(self):

        buffer_5 = self.parcels.copy()
        buffer_4S = [x for x in self.parcels if x.size_index == "Small parcel"]
        buffer_3M = [x for x in self.parcels if x.size_index == "Medium parcel"]


        def find_optimal_combimation(b5, b4S, b3M, savings=0):
            savings5, savings4S, savings3M = 0, 0, 0

            # try to apply discount for first 5 parcels
            if len(b5) >= 5:
                dp5, dc5 = find_min_parcel(b5[:5])

                savings5 = find_optimal_combimation(b5[5:],
                                                    remove_used(b5[:5], b4S),
                                                    remove_used(b5[:5], b3M),
                                                    savings+dc5)

            # try to apply discount for first 4 small parcels
            if len(b4S) >= 4:
                dp4, dc4 = find_min_parcel(b4S[:4])

                savings4S = find_optimal_combimation(remove_used(b4S[:4], b5),
                                                     b4S[4:],
                                                     remove_used(b4S[:4], b3M),
                                                     savings + dc4)

            # try to apply discount for first 5 parcels
            if len(b3M) >= 3:
                dp3, dc3 = find_min_parcel(b3M[:3])

                savings3M = find_optimal_combimation(remove_used(b3M[:3], b5),
                                                     remove_used(b3M[:3], b4S),
                                                     b3M[3:],
                                                     savings + dc3)

            if savings5 == savings4S == savings3M == 0:
                return savings

            # return the best saving
            return max(savings5, savings4S, savings3M)

        def remove_used(to_remove, remove_from):
            c = copy.copy(remove_from)
            for parcel in to_remove:
                if parcel in remove_from:
                    c.remove(parcel)
            return c

        def find_min_parcel(parcels):
            mp = parcels[0]
            mc = parcels[0].cost()

            for i in range(1, len(parcels)):
                if parcels[i].cost() < mc:
                    mc = parcels[i].cost()
                    mp = parcels[i]

            return mp, mc

        return find_optimal_combimation(buffer_5, buffer_4S, buffer_3M)



    def total_cost(self):
        parcel_cost = sum(map(lambda x: x.cost(), self.parcels))

        # handle cost for speedy orders
        parcel_cost = 2 * parcel_cost if self.speedy else parcel_cost

        return parcel_cost

    def print_parcels(self):
        for parcel in self.parcels:
            parcel.print_details()

        print(f"Discounts applied: {self.apply_discounts()}")
        parcels_cost = self.total_cost()
        if self.speedy:
            print(f"Speedy order: ${parcels_cost/2}")

        print(f"Total cost: ${parcels_cost}")


