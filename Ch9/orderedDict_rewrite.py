from collections import OrderedDict

glossary = OrderedDict()

glossary['dictionary'] = 'a collection of key-value pairs'
glossary['key-value pair'] = 'a set of values associated with each other'
glossary['conditional statement'] = 'a statement that evaluates to either true or false'
glossary['for loop'] = 'allows you to do the same action with every item in a list'
glossary['tuple'] = 'an immutable list'
glossary['set'] = 'a list where each item must be unique'
glossary['variable'] = 'a named item that holds a value'
glossary['method'] = 'an action that Python can perform on a piece of data'
glossary['whitespace'] = 'any nonprinting character, such as spaces, tabs, and end-of-line symbols'
glossary['syntax error'] = "occurs when Python doesn't recognize a section of your program as valid Python code"

for word, meaning in glossary.items():
    print(word + "\n\t" + meaning + "\n")