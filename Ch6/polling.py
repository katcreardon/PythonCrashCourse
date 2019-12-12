favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

to_poll = ['sarah', 'jeff', 'aaron', 'phil', 'matt']

for name in to_poll:
    if name in favorite_languages:
        print(name.title() + ", thank you for taking the poll.")
    else:
        print(name.title() + ", please take our poll!")