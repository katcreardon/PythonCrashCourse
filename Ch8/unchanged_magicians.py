def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    great_magicians = ['the Great ' + magician.title() for magician in magicians]
    return great_magicians


magicians = ['harry houdini', 'cardini', 'siegfried & roy', 'david copperfield']

print("\nUnchanged list:")
show_magicians(magicians)

print("\nCopied and changed list:")
show_magicians(make_great(magicians[:]))