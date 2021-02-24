from src.Order import Order

parcels1 = [
    {"size": 1},
    {"size": 2},
    {"size": 15}
]

parcels2 = [
    {"size": 101},
    {"size": 50},
]

def main():
    order1 = Order()
    order1.add(parcels1)

    order2 = Order(speedy=True)
    order2.add(parcels2)

    pretty_print_orders([order1, order2])

def pretty_print_orders(orders):

    for order in orders:
        print("-" * 10 + " ORDER " + "-" * 10)
        order.print_parcels()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


