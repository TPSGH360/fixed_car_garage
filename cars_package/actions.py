from problems_package.problem_menu import problem_list


def car_list(garage):
    print("entering list")
    for car in garage:
        print(
            f"""car name: {car["name"]} - car number:{car["carnumber"]} - car problem: {car["problems"]} - payment:{car["price"]}"""
        )


def car_add(garage):
    print("adding...")
    new_name = input("add the car name:")
    new_number = input("add the car number:")
    new_car = {"name": new_name, "carnumber": new_number}
    new_car = problem_list(new_car)
    print(
        f"""your problems are:{new_car["problems"]}, and will cost you {new_car["price"]}₪ """
    )
    user = input("would you like to add your car to our garage ? (yes/no)")
    if user == "yes":
        garage.append(new_car)
        print("your car has been added to our garage (づ ◕‿◕ )づ ")
    else:
        print("""car addition denied (－_－) zzZ """)
        return


def car_delete(garage):
    print("deleting...")
    user = input("please name the car to remove:")
    for car in garage:
        if (
            user.lower() == car["name"].lower()
            or user.lower() == car["carnumber"].lower()
        ):
            garage.remove(car)
    print("car has been removed")


def search_car(garage):
    print("searching...")
    user = input("please name the car to seach:")
    for car in garage:
        if (
            user.lower() == car["name"].lower()
            or user.lower() == car["carnumber"].lower()
        ):
            print("found")
            print(
                f"""car name: {car["name"]} - car number:{car["carnumber"]} - problem/s:{car["problems"]} - price:{car["price"]}"""
            )
        else:
            print("not found")
