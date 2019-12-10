#1
cat = 'black'
print("Is cat == 'black'? I predict True.")
print(cat == 'black')
#2
print("\nIs cat == 'gray'? I predict False.")
print(cat == 'gray')
#3
print("\nIs cat == 'Black'? I predict False.")
print(cat == 'Black')
#4
name = 'Matt'
print("\nIs name.lower() == 'matt'? I predict True.")
print(name.lower() == 'matt')
#5
print("\nIs name == 'Kathryn' or name == 'Matt'? I predict True.")
print(name == 'Kathryn' or name == 'Matt')
#6
number = 9
print("\nIs number > 2 and number < 8? I predict False.")
print(number > 2 and number < 8)
#7
print("\nIs number != 10? I predict True.")
print(number != 10)
#8
print("\nIs number == 3? I predict False.")
print(number == 3)
#9
colors = ['red', 'blue', 'green', 'yellow']
color = 'purple'
print("\ncolor == 'purple'. Is purple in colors? I predict False.")
print('purple' in colors)
#10
if color not in colors:
    print("\n" + color.title() + " is also a color.")
else:
    print("\nThat is a good color.")