from cars_package.actions import car_list, car_add, car_delete, search_car
from data.save_load import save
from cars_package.caulculation import total_profit, num_of_cars
import sys


def menu(garage):
    num_of_cars(garage), total_profit(garage)
    while True:
        print("Welcome to my garage")
        print("1 - list all cars")
        print("2 - Add a car")
        print("3 - Delete a car")
        print("4 - Search a car")
        print("0 - exit")
        selection = input("what would you like to do?")
        if selection == "1":
            car_list(garage)
        elif selection == "2":
            car_add(garage)
        elif selection == "3":
            car_delete(garage)
        elif selection == "4":
            search_car(garage)
        elif selection == "0":
            print("exiting...")
            save(garage)
            sys.exit()
