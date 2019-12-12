glossary = {'dictionary': 'a collection of key-value pairs',
            'key-value pair': 'a set of values associated with each other',
            'conditional statement': 'a statement that evaluates to either' +
            ' true or false',
            'for loop': 'allows you to do the same action with every item' + 
            ' in a list',
            'tuple': 'an immutable list',
            }

for word in glossary:
    print(word + "\n\t" + str(glossary[word]) + "\n")