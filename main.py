from resources import MENU, resources


# TODO: 1. Print a report of all coffee machine resources. DONE


def current_resources(resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    coins = resources["coins"]
    return [water, milk, coffee, coins]


def store_coins(total):
    # resources["coins"] += total
    return resources["coins"]


def print_resources():
    print(f"The current resources are:\nwater: {current_resources(resources)[0]}\n"
          f"milk: {current_resources(resources)[1]}\n"
          f"coffee: {current_resources(resources)[2]}\n"
          f"money: ${current_resources(resources)[3]}")


def check_resources(water, milk, coffee):
    if water > resources["water"]:
        return False
    elif milk > resources["milk"]:
        return False
    elif coffee > resources["coffee"]:
        return False
    else:
        return True


def check_coins():
    quarters = int(input("How many quarters are you using? "))
    dimes = int(input("How many dimes are you using? "))
    nickels = int(input("How many nickels are you using? "))
    pennies = int(input("How many pennies are you using? "))
    total = .25 * quarters + .10 * dimes + .05 * nickels + .01 * pennies
    return total


def check_successful_transaction():
    if check_resources(water, milk, coffee):
        print(f"Please insert ${coins}.")
        total_amount = check_coins()
        if total_amount >= coins:
            print(f"Here is your {drink} ☕️ Enjoy!")
            store_coins(coins)
            print(f"Please take your change: ${total_amount - coins}")
        else:
            print("Not enough money. Refunding")
    else:
        print("Sorry, we're out of those.")


# TODO: 2. Prompt user by asking “What would you like? (espresso/latte/cappuccino):" DONE
# TODO: 3. Create a Turn off function for the Coffee Machine by entering “off” to the prompt. DONE

machine_on = True
while machine_on:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    water = 0
    milk = 0
    coffee = 0
    coins = 0
    if drink == "off":
        print("Machine powering down for maintenance.")
        machine_on = False
    elif drink == "espresso":
        water = MENU["espresso"]["ingredients"]["water"]
        milk = 0
        coffee = MENU["espresso"]["ingredients"]["coffee"]
        coins = MENU["espresso"]["cost"]
    elif drink == "latte":
        water = MENU["latte"]["ingredients"]["water"]
        milk = MENU["latte"]["ingredients"]["milk"]
        coffee = MENU["latte"]["ingredients"]["coffee"]
        coins = MENU["latte"]["cost"]
        # if check_resources(water, milk, coffee):
        #     print(f"Please insert ${coins}.")
            # if check_coins(coins) >= coins:
            #     print(f"Here is your {drink} ☕️ Enjoy!")
            #     total_amount = check_coins()
            #     store_coins(total_amount)
            # else:
            #     print("Not enough money. Refunding")
    elif drink == "cappuccino":
        water = MENU["cappuccino"]["ingredients"]["water"]
        milk = MENU["cappuccino"]["ingredients"]["milk"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        coins = MENU["cappuccino"]["cost"]
        # if check_resources(water, milk, coffee):
        #     print(f"Please insert ${coins}.")
        #     if check_coins(coins) >= coins:
        #         print(f"Here is your {drink} ☕️ Enjoy!")
        #         total_amount = check_coins()
        #         store_coins(total_amount)
        #     else:
        #         print("Not enough money. Refunding")
    elif drink == "resources":
        print_resources()
    else:
        print("That was not a valid selection. Your money is refunded.")
        # subtract their money from coins if it was already added in.
    check_successful_transaction()

# TODO: 5. Process coins.
""" a. If there are sufficient resources to make the drink selected, then the program should
    prompt the user to insert coins.
    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52 """
# TODO: 6. Check transaction successful?
""" a. Check that the user has inserted enough money to purchase the drink they selected.
    E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
    program should say “Sorry that's not enough money. Money refunded.”.
    b. But if the user has inserted enough money, then the cost of the drink gets added to the
    machine as the profit and this will be reflected the next time “report” is triggered. E.g.
    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5
    c. If the user has inserted too much money, the machine should offer change. 
    E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places."""
# TODO: 7. Make Coffee.
""" a. If the transaction is successful and there are enough resources to make the drink the
    user selected, then the ingredients to make the drink should be deducted from the
    coffee machine resources.
    E.g. report before purchasing latte:
    Water: 300ml
    Milk: 200ml
    Coffee: 100g
    Money: $0
    Report after purchasing latte:
    Water: 100ml
    Milk: 50ml
    Coffee: 76g
    Money: $2.5
    b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
    latte was their choice of drink """
