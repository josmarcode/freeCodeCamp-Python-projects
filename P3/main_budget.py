# import budget
from budget import Category, create_spend_chart

food = Category('Food')
entertainment = Category('Entertainment')
business = Category('Business')

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")

food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

# print(create_spend_chart([business, food, entertainment]))



univ = Category('Universidad')
univ.deposit(900, 'Depósito de papá')
univ.withdraw(300, 'Donas en Bamboo')
univ.withdraw(20, 'Copias')

car = Category('Carro')
car.deposit(200, 'Depósito de mamá')
car.withdraw(150, 'Autolavado')
car.transfer(30, univ)

party = Category('Fiesteo')
party.deposit(300, 'Regalo')
party.withdraw(20, 'Cervezas')

car.transfer(10, party)
univ.transfer(200, party)
party.withdraw(250, 'Servicio de Ron')

ropa = Category('Ropa')
univ.transfer(100, ropa)
ropa.withdraw(90, 'Pantalón')

"""
print(univ.get_balance(), '\n')
print(ropa.get_balance(), '\n')
print(car.get_balance(), '\n')
print(party.get_balance(), '\n\n =========== \n\n')
"""

print(univ)
print('\n')
print(car)
print('\n')
print(party)
print('\n')
print(ropa)
print('\n')

print(create_spend_chart([univ, ropa, car, party]))
