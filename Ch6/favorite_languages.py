favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

print("Sarah's favorite language is " + favorite_languages['sarah'].title() +
      ".")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# looping through keys is default behavior; keys() method not needed
for name in favorite_languages.keys():
    print(name.title())
    
friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# looping through a dictionary's keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
    
# looping through all values in a dictionary without checking for repeats
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# sets only contain unique items
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
    
# store list of languages
favorite_languages= {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phill': ['python', 'haskell'],
        }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())