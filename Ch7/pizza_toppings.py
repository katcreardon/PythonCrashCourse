prompt = "\nPlease enter the toppings you want:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print("I will add " + topping + " to your pizza.")