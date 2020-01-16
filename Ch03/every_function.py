languages = ['English', 'Latin', 'French', 'Spanish']

print(languages[2])
print(languages[-1])
print(languages[0].upper())

message = "My first language was " + languages[0] + "."
print(message)

languages[0] = 'Elvish'
print(languages)

languages.append('English')
languages.insert(1, 'Middle English')
print(languages)

del languages[3]
print(languages)

languages.remove('Latin')
print(languages)

popped_language = languages.pop(0)
print(popped_language + " isn't a real language, so it shouldn't be in this " +
        "list.")
print(languages)

print(sorted(languages))
print(sorted(languages, reverse=True))

languages.append('Welsh')
languages.append('Tagalog')
languages.sort()
print(languages)

languages.reverse()
print(languages)

print("The final length of the list is " + str(len(languages)) + ".")
