class Category:
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []

    def __repr__(self):
        return f"Category({self.category_name})"

    def __str__(self):
        #TODO: complete this
        output_table = self.category_name.center(30, '*') + '\n'
        for transaction in self.ledger:
            description, amount = transaction["description"], transaction['amount']
            amount = f"{amount:.2f}"
            output_table += description[:23].ljust(23) + amount.rjust(7) + '\n'
        output_table += f"Total: {self.get_balance()}"
        return output_table

    def deposit(self, amount, description=None):
        if description is None:
            description = ""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=None):
        transfer_possible = self.check_funds(amount)
        if description is None:
            description = ""
        if transfer_possible:
            self.ledger.append({"amount": -amount, "description": description})
        return transfer_possible

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self, amount, category):
        transfer_possible = self.check_funds(amount)
        if transfer_possible:
            self.withdraw(amount,  f"Transfer to {category.category_name}")
            category.deposit(amount, f"Transfer from {self.category_name}")
        return transfer_possible

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def amount_spent(self):
        amount_spent = 0
        for transaction in self.ledger:
            amount = transaction["amount"]
            if amount < 0: # check if trasaction was a withdrawal
                amount_spent += abs(amount)
        return amount_spent
                

def create_spend_chart(categories):
    # 1st half of the table.
    category_wise_spending = [category.amount_spent() for category in categories]
    total = sum(category_wise_spending)
    spending_percent = [round(amount / total * 100) for amount in category_wise_spending]
    output_table = "Percentage spent by category\n"
    for percentage in range(100, -1, -10):
        output_table += f"{percentage}|".rjust(4)
        for quantity in spending_percent:
            output_table += (' o ' if percentage <= quantity else " " * 3)
        output_table += ' \n' # new line

    # Table divider
    output_table += " " * 4 + "-" * (3 * len(categories) + 1) + "\n"

    # 2nd half of the table.
    category_names = [category.category_name for category in categories]
    largest_category_names = max(category_names, key=len)
    for i in range(len(largest_category_names)):
        output_table += " " * 4
        for name in category_names:
            try:
                output_table += name[i].center(3)
            except IndexError:
                output_table += " " * 3
        output_table += ' \n'
    return output_table[:-1]