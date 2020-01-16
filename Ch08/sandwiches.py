def make_sandwich(*toppings):
    """Summarize the sandwich we are about to make."""
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_sandwich('bacon', 'lettuce', 'tomato', 'mayo')
make_sandwich('American cheese')
make_sandwich('turkey', 'mayo', 'mustard')