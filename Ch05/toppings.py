requested_topping = 'mushrooms'

# compare values and print string if no match
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
    
requested_toppings = ['mushrooms', 'extra cheese', 'onions', 'pineapple']
# check for values in list
print('mushrooms', 'mushrooms' in requested_toppings)
print('pepperoni', 'pepperoni' in requested_toppings)

# every condition is evaluated
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# conditional statements inside for loops
for requested_topping in requested_toppings:
    if requested_topping == 'onions':
        print("Sorry, we are out of onions right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

requested_toppings = []
# checks if list has at least one item
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")