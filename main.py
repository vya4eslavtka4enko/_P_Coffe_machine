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
select_drink = input("What would you like? (espresso/latte/cappuccino)")
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def select_user(select_drink, resources):
    if select_drink == 'expresso':
        for k, v in MENU.items():
            if k == 'expresso':
                cost = v['cost']
        print("Here is your expresso! Enjoy ")
    elif select_drink == 'latte':
        for k, v in MENU.items():
            if k == 'latte':
                cost = v['cost']
        print("Here is your latte! Enjoy ")
    elif select_drink == 'cappuccino':
        for k, v in MENU.items():
            if k == 'cappuccino':
                cost = v['cost']
        print("Here is your cappuccino! Enjoy ")
    elif select_drink == 'report':
        for item in resources.items():
            print(item)
    return cost
def insert_coin():
    print('Please insert coins. ')
    quarters = int(input("How many quarters? "))  #25
    dimes = int(input("How many dimes? "))  #10
    nickles = int(input("How many nickles? "))  #5
    pennies = int(input("How many pennies? "))   #1
    sum_quarters = quarters * 25 / 100
    sum_dimes = dimes * 10 / 100
    sum_nickles = nickles * 5 / 100
    sum_pennies = pennies * 1 / 100
    sum_coin = sum_quarters+sum_dimes+sum_nickles+sum_pennies
    cost = select_user(select_drink, resources)
    sum_coin-=cost
    print("{:.2f}".format(sum_coin))

select_user(select_drink, resources)
insert_coin()
