def shipping_rate(
    weight_of_package, miles
):  # a function that calculates conditions of the weight of the packedge, and miles, and returns the shipping price

    price = 0.00

    rate = miles / 500.00
    if user_miles % 500 > 0:
        rate = (user_miles + (500 - (user_miles % 500))) / 500

    if weight_of_package <= 2:
        price = rate * 1.10

    elif (weight_of_package > 2) and (weight_of_package <= 6):
        price = rate * 2.20

    elif (weight_of_package > 6) and (weight_of_package <= 10):
        price = rate * 3.70

    elif weight_of_package > 10:
        price = rate * 4.80

    return price


package = 1  # a variable that assumes that there is atleast one package

while (
    package == 1
):  # a while loop that iterates each time whether someone wants to enter another packedge
    user_weight = 0.00
    user_miles = 0.00
    user_weight = float(
        input("Enter Package Weight: ")
    )  # obtains the weight of the packedge, and prompts the user user to give an input accordingly
    user_miles = float(
        input("Enter Distance: ")
    )  # obtains the distance that the packedge will travel, and prompts the user user to give an input accordingly
    print()

    while (
        user_weight < 0 or user_miles < 0
    ):  # A loop that generates an error if the weight of the packedge and the miles are below zero, and tells you to give a positve value
        if user_weight < 0:
            user_weight = float(input("Enter a positive package Weight: "))
        else:
            print("Please enter a positive distance")
            user_miles = float(input("Enter a positive Distance: "))
    else:
        print(f"The shipping cost is: ${shipping_rate(user_weight, user_miles):.2f}")
        mpackage = input("Would you like to calculate shipping on another package?: ")
        print()
        if mpackage == ("No" or "no"):
            package = 0
        else:
            continue
