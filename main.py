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
    "money": 0,
}

def coins_total():
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    quarters_amount = float(quarters) * .25
    dimes_amount = float(dimes) * .10
    total = quarters_amount + dimes_amount
    print(f"Your total money is {total}")
#test coins_total f(x)
coins_total()
# while machine_on True:
# TODO: Print a resource report
for key, value in resources.items():
    print(key, ':', value)

# TODO: input "What would you like?
drink = input("\nWhat would you like? (espresso/latte/cappuccino):")
# TODO: make an off feature by using the word "off"
if drink == 'off':
    # machine_on False
    print("The machine is now closed.")
# TODO: are there enough resources to make a drink?
if drink == "espresso":
    if resources[0] >= 50:
        print("do something here")
        if resources[1] >= 18:
            print("Please enter $1.50 in US coins")
            coin_total()
        else:
            print("Sorry, there is not enough coffee.")
    else:
        print("Sorry, there is not enough water.")
elif drink == "latte":
   if resources.water >= 200:
       print("do something here")
       if milk >= 150:
           print("do something here")
           if coffee >= 24:
               print("do something here")
           else:
               print("Sorry, there is not enough coffee")
       else:
           print("Sorry, there is not enough milk.")
   else:
       print("Sorry, there is not enough water.")
elif drink == "cappuccino":
    if resources.water >= 250:
        print("do something here")
        if milk >= 100:
            print("do something here")
            if coffee >= 24:
                print("do something here")
            else:
                print("Sorry, there is not enough coffee")
        else:
            print("Sorry, there is not enough milk.")
    else:
           print("Sorry, there is not enough water.")

    # TODO: Process coins (US coins)

    # TODO: Make drinks

    # TODO: friendly end message after drink dispensed
    print("Have a caffeinated day!")
