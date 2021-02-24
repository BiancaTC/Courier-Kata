SIZE_COST = [3, 8, 15, 25]
SIZE_NAME = ["Small parcel", "Medium parcel", "Large parcel", "XL parcel"]


class Parcel:

    def __init__(self, size):
        self.size_index = self.calculate_size_index(size)


    def cost(self):
        cost = SIZE_COST[self.size_index]
        return cost

    def calculate_size_index(self, size):
        if size < 10:
            return 0
        elif size < 50:
            return 1
        elif size < 100:
            return 2
        else:
            return 3

    def print_details(self):
        type = SIZE_NAME[self.size_index]
        cost = SIZE_COST[self.size_index]
        print(f"{type}: ${cost}")
