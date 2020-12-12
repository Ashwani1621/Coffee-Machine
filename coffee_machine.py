# Coffee maker - Creating a class to control everything
class CoffeeMaker:
    # The main function, where the initial input will choose the posterior function
    def __init__(self):
        # Coffee maker - Initial supplies
        self.supplies = {"money": 550, "water": 400, "milk": 540, "coffee beans": 120, "cups": 9}
        self.supplies_after = self.supplies.copy()

    # Print current the machine supplies
    def machine_supplies(self):
        print()
        print(f"The coffee machine has:\n"
              f"{self.supplies['water']} of water\n"
              f"{self.supplies['milk']} of milk\n"
              f"{self.supplies['coffee beans']} of coffee beans\n"
              f"{self.supplies['cups']} of disposable cups\n"
              f"${self.supplies['money']} of money")
        print()
        self.coffee_input_begin()

    # What is needed to make espresso and the others, subtract then from supplies and sum money
    def espresso(self):
        self.supplies_after = self.supplies.copy()
        self.supplies_after['water'] -= 250
        self.supplies_after['coffee beans'] -= 16
        self.supplies_after['money'] += 4
        self.supplies_after['cups'] -= 1
        return self.supplies_after

    def latte(self):
        self.supplies_after = self.supplies.copy()
        self.supplies_after['water'] -= 350
        self.supplies_after['coffee beans'] -= 20
        self.supplies_after['milk'] -= 75
        self.supplies_after['money'] += 7
        self.supplies_after['cups'] -= 1
        return self.supplies_after

    def cappuccino(self):
        self.supplies_after = self.supplies.copy()
        self.supplies_after['water'] -= 200
        self.supplies_after['coffee beans'] -= 12
        self.supplies_after['milk'] -= 100
        self.supplies_after['money'] += 6
        self.supplies_after['cups'] -= 1
        return self.supplies_after

    def supply_checker(self, remaining):
        # global supplies
        count = 0
        for key, value in remaining.items():
            if value < 0 and key != "money":
                print(f"Sorry, not enough {key}!")
                print()
                self.coffee_input_begin()
            else:
                count += 1
        if count == 5:
            print("I have enough resources, making you a coffee!")
            print()
            self.supplies = remaining
            self.coffee_input_begin()
        else:
            self.coffee_input_begin()

    # When the action is buy, execute the functions according to the coffee option
    def buy(self):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, "
                            "back - to main menu:")
        if coffee_type == "1":
            self.supply_checker(self.espresso())
            # machine_supplies()
        elif coffee_type == "2":
            self.supply_checker(self.latte())
            # machine_supplies()
        elif coffee_type == "3":
            self.supply_checker(self.cappuccino())
            # machine_supplies()
        elif coffee_type == "back":
            self.coffee_input_begin()

    # When the action is to fill supplies in the machine
    def fill(self):
        self.supplies['water'] += int(input("Write how many ml of water do you want to add:"))
        self.supplies['milk'] += int(input("Write how many ml of milk do you want to add:"))
        self.supplies['coffee beans'] += int(input("Write how many grams of coffee beans do you want to add:"))
        self.supplies['cups'] += int(input("Write how many disposable cups of coffee do you want to add:"))
        self.coffee_input_begin()
        # print()
        # machine_supplies()

    # When the action is from take the money from the machine
    def take(self):
        print()
        print(f"I gave you ${self.supplies['money']}")
        self.supplies['money'] = 0
        print()
        self.coffee_input_begin()
        # machine_supplies()

    def coffee_input_begin(self):
        action = input("Write action (buy, fill, take, remaining, exit)")
        if action == "take":
            self.take()
        elif action == "fill":
            self.fill()
        elif action == "remaining":
            self.machine_supplies()
        elif action == "exit":
            exit()
        elif action == "buy":
            self.buy()

        # coffee_input_begin()

    def start(self):
        self.coffee_input_begin()


coffee = CoffeeMaker()
coffee.start()