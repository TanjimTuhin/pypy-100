from art import coffeeshop,closed,pay
print(coffeeshop)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Do 1:taking input “What would you like? (espresso/latte/cappuccino):”

#Do 2:Check resources sufficient?
while True:
    flavour=input('What would you like? (espresso/latte/cappuccino) or type "off" to shut down or report:')
    if flavour=="off".lower():
        print(closed)
        exit()
    elif flavour=='report':
        print(resources)
        continue
    elif flavour in MENU:
        if resources["water"] >= MENU[flavour]["ingredients"]["water"]:
            if "milk" not in MENU[flavour]["ingredients"] or resources["milk"] >= MENU[flavour]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU[flavour]["ingredients"]["coffee"]:
                    print('Ingradient Available')
                else:
                    print('Not enough coffee')
                    break
            else:
                print('Not enough milk')
                break
        else:
            print('Not enough water')
            break
    else:
        print('Invalid Selection')
    cost=MENU[flavour]["cost"]
    print(f"{flavour} cost: {cost:.2f}" )
                
    #Do 3:input and process coin
    print(pay)
    print('Please insert coins:')
    quarters=int(input('how many quarters?:'))
    dimes=int(input('how many dimes?:'))
    nickles=int(input('how many nickles?:'))
    pennies=int(input('how many pennies?:'))
    #Do 4:calculate the total cost
    total_cost=quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
    print(f"you give ${total_cost:.2f} ")
    #Do 5:check if transaction is successful
    if total_cost >= cost:
        print(f"Here is your {flavour} and ${total_cost-cost:.2f}")
        resources["water"] -= MENU[flavour]["ingredients"]["water"]
        # Check if milk is needed for the selected drink before deducting
        if "milk" in MENU[flavour]["ingredients"]:
            resources["milk"] -= MENU[flavour]["ingredients"]["milk"]
        resources["coffee"] -= MENU[flavour]["ingredients"]["coffee"]
    else:
        print('Sorry that\'s not enough money. Money refunded.')
        print(f'Here is your ${total_cost:.2f}')




