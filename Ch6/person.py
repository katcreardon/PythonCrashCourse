person_0 = {'first_name': 'Jay',
          'last_name': 'Gatsby',
          'age': 30,
          'city': 'New York City',
          }

print(person_0['first_name'])
print(person_0['last_name'])
print(person_0['age'])
print(person_0['city'])

person_1 = {'first_name': 'Harry',
            'last_name': 'Potter',
            'age': 11,
            'city': 'Little Whinging',
            }

person_2 = {'first_name': 'Sophie',
            'last_name': 'Hatter',
            'age': 18,
            'city': 'Market Chipping',
            }

people = [person_0, person_1, person_2]

for person in people:
    print(person)