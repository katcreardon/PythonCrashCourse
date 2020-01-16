def make_shirt(size, message='I love Python'):
    """Displays the size and message printed on a shirt."""
    print("\nYour shirt is size " + size + " and says '" + message + "'.")


make_shirt('S', 'This function call uses positional arguments')
make_shirt(message='This function call uses keyword arguments', size='XL')
make_shirt('L')
make_shirt('M')
make_shirt('XS', 'This function provides an argument for the message' +
           ' parameter')
