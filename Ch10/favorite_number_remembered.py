import json

def get_stored_number():
    """Get stored number if available."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number

def get_new_number():
    """Prompt for a new number."""
    number = input("What is your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    return number

def greet_user():
    """Greet the user."""
    number = get_stored_number()
    if number:
        print("I know your favorite number! It's " + number + "!")
    else:
        number = get_new_number()
        print("We'll remember that your favorite number is " + number + " when you come back!")

greet_user()