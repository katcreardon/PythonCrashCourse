glossary = {'dictionary': 'a collection of key-value pairs',
            'key-value pair': 'a set of values associated with each other',
            'conditional statement': 'a statement that evaluates to either' +
            ' true or false',
            'for loop': 'allows you to do the same action with every item' + 
            ' in a list',
            'tuple': 'an immutable list',
            'set': 'a list where each item must be unique',
            'variable': 'a named item that holds a value',
            'method': 'an action that Python can perform on a piece of data',
            'whitespace': 'any nonprinting character, such as spaces, tabs' +
            ', and end-of-line symbols',
            'syntax error': "occurs when Python doesn't recognize a section" +
            " of your program as valid Python code",
            }

for word, meaning in glossary.items():
    print(word + "\n\t" + meaning + "\n")