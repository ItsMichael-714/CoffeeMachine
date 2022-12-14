from resources import MENU, resources


# Print a report of all coffee machine resources. DONE


def current_resources(resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    coins = resources["coins"]
    return [water, milk, coffee, coins]


def store_coins(total):
    resources["coins"] += total
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee
    print(resources)


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


# Process coins. DONE


def check_coins():
    quarters = int(input("How many quarters are you using? "))
    dimes = int(input("How many dimes are you using? "))
    nickels = int(input("How many nickels are you using? "))
    pennies = int(input("How many pennies are you using? "))
    total = .25 * quarters + .10 * dimes + .05 * nickels + .01 * pennies
    return total


# Check transaction successful? DONE
# Make Coffee. DONE

def check_successful_transaction():
    if check_resources(water, milk, coffee):
        print(f"Please insert ${coins}.")
        total_amount = check_coins()
        if total_amount >= coins:
            print(f"Here is your {drink} ☕️ Enjoy!")
            store_coins(coins)
            print(f"Please take your change: ${round(total_amount - coins, 2)}")
        else:
            print("Not enough money. Refunding")
    else:
        print("Sorry, we're out of those.")


# Prompt user by asking “What would you like? (espresso/latte/cappuccino):" DONE
# Create a Turn off function for the Coffee Machine by entering “off” to the prompt. DONE

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
        check_successful_transaction()
    elif drink == "latte":
        water = MENU["latte"]["ingredients"]["water"]
        milk = MENU["latte"]["ingredients"]["milk"]
        coffee = MENU["latte"]["ingredients"]["coffee"]
        coins = MENU["latte"]["cost"]
        check_successful_transaction()
    elif drink == "cappuccino":
        water = MENU["cappuccino"]["ingredients"]["water"]
        milk = MENU["cappuccino"]["ingredients"]["milk"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        coins = MENU["cappuccino"]["cost"]
        check_successful_transaction()
    elif drink == "resources":
        print_resources()
    else:
        print("That was not a valid selection.")
        # subtract their money from coins if it was already added in.



