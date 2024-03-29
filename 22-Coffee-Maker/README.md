# Coffee Machine README

## main.py

The `main.py` script is the main driver of the coffee machine program. It orchestrates the interaction between the user, the menu, the coffee maker, and the money machine. The script runs a loop allowing the user to choose drinks, turn off the machine, or request a report on the machine's status.

## menu.py

The `menu.py` module defines the `Menu` class, which models the menu of the coffee machine. It contains a list of `MenuItem` objects, each representing a drink with its name, required ingredients (water, milk, coffee), and cost. The `Menu` class provides methods to get a list of available drinks and find a specific drink based on the user's order.

## machine_money.py

The `machine_money.py` module defines the `MoneyMachine` class, modeling the money-related operations of the coffee machine. It handles the processing of coins, making payments, and keeping track of the machine's profit. The class includes coin values, methods to report profits, process inserted coins, and handle payments.

## coffee_maker.py

The `coffee_maker.py` module defines the `CoffeeMaker` class, modeling the machine responsible for making coffee. It maintains a dictionary of available resources (water, milk, coffee) and provides methods to report resource levels, check resource sufficiency for a given drink, and make a coffee by deducting the required resources.

These modules collectively create a coffee machine simulation where users can choose drinks, insert coins, and enjoy their beverages. The system ensures proper resource management, handles payments, and maintains a record of profits. The modular design allows for easy extension and maintenance of the coffee machine functionality.

# The code file by file:

### `main.py`

```python
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
```

- **Imports**: Import necessary classes from other modules (`Menu`, `CoffeeMaker`, `MoneyMachine`).

```python
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
```

- **Instances**: Create instances of `MoneyMachine`, `CoffeeMaker`, and `Menu`.

```python
is_on = True
```

- **Loop Control**: Initialize a variable `is_on` to control the main loop.

```python
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
```

- **Main Loop**: Continuously prompts the user for input until turned off.
- **User Input**: Get user input for drink selection or machine actions.
- **Conditions**: Check user input for turning off the machine or generating reports.
- **Make Drink**: If a drink is selected, check resources and make the drink if conditions are met.

### `menu.py`

```python
class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
```

- **MenuItem Class**: Defines a class to model each menu item with its name, cost, and ingredients.

```python
class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]
```

- **Menu Class**: Defines a class to model the menu with a list of predefined drinks.

```python
    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
```

- **`get_items` Method**: Returns a string with the names of available menu items.

```python
    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
```

- **`find_drink` Method**: Searches for a drink by name and returns the item if found.

### `money_machine.py`

```python
class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
```

- **MoneyMachine Class**: Models the money machine with currency and coin values.

```python
    def __init__(self):
        self.profit = 0
        self.money_received = 0
```

- **Initialization**: Initializes profit and money received variables.

```python
    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")
```

- **`report` Method**: Prints the current profit.

```python
    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received
```

- **`process_coins` Method**: Takes user input for coin quantities and calculates the total received.

```python
    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
```

- **`make_payment` Method**: Processes the payment, checks if it's sufficient, and provides change.

### `coffee_maker.py`

```python
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
```

- **CoffeeMaker Class**: Models the machine that makes coffee with initial resource levels.

```python
    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
```

- **`report` Method**: Prints a report of all resources.

```python
    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make
```

- **`is_resource_sufficient` Method**: Checks if there are enough resources to make a drink.

```python
    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
```

- **`make_coffee` Method**: Deducts the required ingredients from the resources and prints a message about enjoying the coffee.