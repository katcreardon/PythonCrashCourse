favorite_numbers = {'Alice': [3, 5, 7],
                    'Bob': [9, 42, 12, 17],
                    'Carol': [21, 5],
                    'David': [100, 101],
                    'Eve': [36],
                    }

for person in favorite_numbers:
    print(person + "'s favorite numbers: " + str(favorite_numbers[person]))