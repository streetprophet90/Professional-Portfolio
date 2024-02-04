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

