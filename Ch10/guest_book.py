filename = 'guest_book.txt'

prompt = "\nWhat is your name?"
prompt += "\n(Enter 'quit' when you are finished.) "

# loop runs forever unless it reaches break statement
while True:
    name = input(prompt)
    if name == 'quit':
        break
    else:
        print("Welcome, " + name.title() + "!")
        with open(filename, 'a') as file_object:
            file_object.write(name.title() + "\n")