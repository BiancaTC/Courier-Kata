PARCELS_CONSTANTS = {
    "Small parcel": {
        "size_limit": 10,
        "cost": 3,
        "weight_limit": 1
    },
    "Medium parcel": {
        "size_limit": 50,
        "cost": 8,
        "weight_limit": 3
    },
    "Large parcel": {
        "size_limit": 100,
        "cost": 15,
        "weight_limit": 6
    },
    "XL parcel": {
        "cost": 25,
        "weight_limit": 10
    }
}

class Parcel:

    def __init__(self, size, weight=0):
        self.size_index = self.calculate_size_index(size)
        self.weight = weight

    def cost(self):
        # initial parcel weight
        cost = PARCELS_CONSTANTS[self.size_index]["cost"]

        # parcel extra weight
        cost += self.calculate_extra_weight() * 2

        return cost

    def calculate_extra_weight(self):
        return max(self.weight - PARCELS_CONSTANTS[self.size_index]["weight_limit"], 0)

    def calculate_size_index(self, size):
        if size < PARCELS_CONSTANTS["Small parcel"]["size_limit"]:
            return "Small parcel"
        elif size < PARCELS_CONSTANTS[ "Medium parcel"]["size_limit"]:
            return "Medium parcel"
        elif size < PARCELS_CONSTANTS["Large parcel"]["size_limit"]:
            return "Large parcel"
        else:
            return "XL parcel"

    def print_details(self):
        parcel_type = self.size_index
        cost = self.cost()
        print(f"{type}: ${cost}")
        extra_weight = self.calculate_extra_weight()
        if extra_weight:
            print(f"[*] extra weight: {extra_weight} kg")
