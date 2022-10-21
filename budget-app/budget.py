class Category:

    #construct the categories.
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0.0

    #create the amount of categories.
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    #decrease the amount by withdraw if there is enough.
    def withdraw(self, amount, description=""):
        if self.balance - amount >= 0:
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        return False

    #check the current balance.
    def get_balance(self):
        return self.balance

    #transfer some amount from a category to another category, if there is enough.
    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    #chech some amount if you have.
    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        return False

    #print final situation.
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output

#Construct the percentage table.
def create_spend_chart(categories):
    spent_amounts = []
    # Get total spent in each category
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    # Calculate percentage rounded down to the nearest 10
    total = round(sum(spent_amounts), 2)
    spent_percentage = list(
        map(lambda amount: int((((amount / total) * 10) // 1) * 10),
            spent_amounts))

    # Create the bar chart substrings
    header = "Percentage spent by category\n"
    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.name, categories))
    max_length = max(map(lambda name: len(name), descriptions))
    descriptions = list(map(lambda name: name.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")