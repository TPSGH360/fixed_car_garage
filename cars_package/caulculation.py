def num_of_cars(garage):
    count = len(garage)
    print(f"Currently there are {count} cars in my garage,")


def total_profit(garage):
    total_price = sum(car["price"] for car in garage)
    print(f"The current profit is:{total_price}.")
