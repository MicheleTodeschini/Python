# collection = single variable used to store multiple values
# List = [] ordered and changeable, Duplicates OK
# Set = {} Unordered and immutable, but Add/remove OK, no duplicates
# Tuple = () Ordered and unchangeable. Duplicates OK, FASTER

""" fruits  = ['apple', 'ananas']

print(fruit) """

# Shopping cart program

foods = []
prices = []
total = 0 

while True:
    food = input('What food to buy (q to quit): ')
    if food.lower() == "q":
        break
    else:
        price = float(input(f'Enter the price of a {food}: '))
        foods.append(food)
        prices.append(price)
    
print('----YOUR CART----')

for food in foods:
    print(food, end=' ')

for price in prices:
    total += price

print(f'Your total is €{total}')