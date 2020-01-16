def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    magicians[:] = ['the Great ' + magician.title() for magician in magicians]


magicians = ['harry houdini', 'cardini', 'siegfried & roy', 'david copperfield']
make_great(magicians)
show_magicians(magicians)