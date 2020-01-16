pizzas = ['Hawaiian', 'margherita', 'olive and mushroom']
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print("I like " + pizza + " pizza.")
print("I really love pizza!\n")

friend_pizzas = pizzas[:]

pizzas.append('capers, anchovies, and red onions')
friend_pizzas.append('pepperoni')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
