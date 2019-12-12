sandwich_orders = ['Reuben', 'pastrami', 'ham', 'pastrami', 'BLT', 
                   'club', 'veggie', 'pastrami']

finished_sandwiches = []

print("The deli has run out of pastrami.")

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    current_order = sandwich_orders.pop()
    print("I made your " + current_order + " sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)