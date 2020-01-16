hope = {
        'kind of animal': 'dog', 
        'owner': 'john',
        }

stella = {
        'kind of animal': 'cat',
        'owner': 'becca',
        }

joker = {
        'kind of animal': 'cat',
        'owner': 'kathryn',
        }

murphy = {
        'kind of animal': 'dog',
        'owner': 'anne',
        }

pets = [hope, stella, joker, murphy]

for pet in pets:
    for key, value in pet.items():
        print(key + ": " + value)

