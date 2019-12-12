favorite_places = {
        'alice': ['the beach', 'the mountains'],
        'bob': ['Paris', 'the park', 'the lake'],
        'carol': ['home'],
        }

for person, places in favorite_places.items():
    if len(places) < 2:
        print(person.title() + "'s favorite place is:\n\t" + places[0])
    else:
        print(person.title() + "'s favorite places are:")
        for place in places:
            print("\t" + place)