filename = 'responses.txt'

prompt = "\nWhy do you like programming?"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    response = input(prompt)
    if response == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(response + "\n")