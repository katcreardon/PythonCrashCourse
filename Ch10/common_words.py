def count_the(filename):
    """Count the number of occurrences of the word 'the' in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count the number of 'the' in the file.
        number = contents.count('the')
        print("The file " + filename + " has " + str(number) + " occurrences of the word 'the'.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_the(filename)