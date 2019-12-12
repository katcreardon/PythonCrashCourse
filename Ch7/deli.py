sandwich_orders = ['Reuben', 'ham', 'BLT', 'club', 'veggie']

finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I made your " + current_order + " sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
    