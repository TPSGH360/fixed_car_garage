# caulculation & menu (combined in the same function)


def problem_list(new_car):
    problem = []
    price = []
    while True:
        print("here is a list of common problems:")
        print("1 - Engine - - 2000 ₪")
        print("2 - Brakes  - - 1000 ₪")
        print("3 - 5000 km treatment - 500 ₪")
        print("4 - 10,000 km treatment - 1000 ₪")
        print("5 - Filters + Oil - 250 ₪")
        print("6 - Gear - 1000 ₪")
        print("7 - confirm ?")
        selection = input("please select a problem:")
        if selection == "1":
            problem.append("engine")
            price.append(2000)
            print(problem, price)
        elif selection == "2":
            problem.append("brakes")
            price.append(1000)
            print(problem, price)
        elif selection == "3":
            problem.append("5k treatment")
            price.append(500)
            print(problem, price)
        elif selection == "4":
            problem.append("10k treatment")
            price.append(1000)
            print(problem, price)
        elif selection == "5":
            problem.append("Filters + Oil ")
            price.append(250)
            print(problem, price)
        elif selection == "6":
            problem.append("gear")
            price.append(1000)
            print(problem, price)
        elif selection == "7":  # < --- כאן נתקענו
            total_price = int(sum(price))
            # print(total_price)
            new_car["problems"] = problem
            new_car["price"] = total_price
            return new_car
