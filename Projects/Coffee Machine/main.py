import details as dt


def evaluation(coffee_type):
    if dt.resources["water"]>dt.menu[coffee_type]["ingredients"]["water"] and dt.resources["milk"]>dt.menu[coffee_type]["ingredients"]["milk"]:
        if dt.resources["coffee"] > dt.menu[coffee_type]["ingredients"]["coffee"]:
            dt.resources["water"] = dt.menu[coffee_type]["ingredients"]["water"] - dt.menu[coffee_type]["ingredients"]["water"]
            dt.resources["milk"] = dt.menu[coffee_type]["ingredients"]["milk"] - dt.menu[coffee_type]["ingredients"]["milk"]
            dt.resources["coffee"] = dt.menu[coffee_type]["ingredients"]["coffee"] - dt.menu[coffee_type]["ingredients"]["coffee"]
            return 1
        else:
            print("Sorry not enough ingredients! Come back later :) ")
            return 0
    else:
        print("Sorry not enough ingredients! Come back later :) ")
        return 0


def money_conversion(quarters, dimes, nickels, pennies):
    total = (quarters*0.25)+(dimes*0.10)+(nickels*0.05)+(pennies*0.01)
    return total


flag = True
while flag:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    flag = evaluation(coffee_type)
    if (flag == 0):
        exit()
    print("Please insert coins ")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    money = money_conversion(quarters, dimes, nickels, pennies)

    if money > dt.menu[coffee_type]["cost"]:
        print("Here's ur change: ", round(money - dt.menu[coffee_type]["cost"], 2))
        print(f"Your {coffee_type} is ready enjoy :) ")
    elif money == dt.menu[coffee_type]["cost"]:
        print(f"Here is your {coffee_type} enjoy :) ")






