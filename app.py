from data.save_load import load
from cars_package.menu import menu


def main():
    garage = load()
    menu(garage)


if __name__ == "__main__":
    main()


# I tried to fix an error function and I didn't succeed (more precisely we didn't succeed) and without it quite a large part of the project didn't work...
# Without the function of problem_list() everything works.

# ** Another note exit() didn't work for me even then I brought the external import sys.


# the fixes:
# 1) the vars "problem" and "price" were that they were in the while loop, which caused them to restart and repeat every time i entered it.
# 2) i wrote in the function "problem_list(garage):" and caused it to return every time the whole content of my json instead of only the car i'm adding.
# 3) i wrote "return" which caused the function problem_list() to remember what i did but it didnt transfer to the added car. was solved via "return new_car"
# 4) also finished the whole exercise...
#    ***added the functions - num_of_cars(garage), total_profit(garage)| updated car_add(garage)| added Packages and modules.
