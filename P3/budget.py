class Category:

    def __init__(self, name):
        self.ledger = []
        self.categ = name
        self.balance = 0

    def __str__(self):
        pre = '*' * ((30 - len(self.categ)) // 2)           # For heading
        pos = '*' * (30 - (len(pre) + len(self.categ)))
        self.body = ''

        self.body += f'{pre}{self.categ}{pos}'              # Heading
        for move in self.ledger:
            # Spaces for alignment
            spc = ' ' * \
                (30 - len(move['description'][:23]) -
                 len(format(move['amount'], '.2f')))
            # Movements
            self.body += f'\n{move["description"][:23]}{spc}{move["amount"]:.2f}'

        self.body += f'\nTotal: {self.balance:.2f}'         # Total

        return self.body

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        if self.balance - amount >= 0:
            return True
        else:
            return False

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False

    def transfer(self, amount, name):
        if self.check_funds(amount):
            # self's ledger modify
            self.ledger.append(
                {"amount": -amount, "description": f'Transfer to {name.categ}'})
            # updating self balance
            self.balance -= amount
            # other's ledger modify
            name.ledger.append(
                {"amount": amount, "description": f'Transfer from {self.categ}'})
            # updating other balance
            name.balance += amount
            return True
        else:
            return False


def create_spend_chart(categories):
    dataset = {}    # {'Category': [Spend, Percentage, Bar_string], ...}

    # Calculating spends for categories
    for element in categories:
        a = 0
        for move in element.ledger:
            if move['amount'] < 0:
                a -= move['amount']
            dataset[element.categ] = [a]

    # print(dataset)

    total = sum([dataset[key][0] for key in dataset])   # Total spented

    # Calculating spends for categories in percentage
    for data in dataset:
        percentage = (dataset[data][0] * 100 // total // 10) * 10   # Truncate
        dataset[data].append(percentage)

        # Preparing bars for printing
        dataset[data].append(
            ' ' * int((10 - percentage // 10)) + 'o' * int((percentage // 10) + 1))

    # Printing chart process
    printing = 'Percentage spent by category'   # Heading

    for i in range(11):
        num = (-10 * i) + 100
        printing += f'\n{" " * (3 - len(str(num)))}{num}|'      # Percentages
        for key, value in dataset.items():
            printing += f' {value[2][i]} '                      # Bars sliced
        printing += ' '

    printing += f'\n{" " * 4}{"-" * (3 * len(categories) + 1)}'

    # length of the longest word
    r = max([len(key) for key in dataset])
    for i in range(r):
        printing += f'\n{" " * 4}'
        for key in dataset:
            try:
                printing += f' {key[i]} '
            except:
                printing += '   '
        printing += ' '

    return printing
