players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])
print(players[1:4])

# Omitting the first index automatically starts the slice at the beginning
print(players[:4])
# Omitting the second index returns items through the end of the list
print(players[2:])
# A negative index i outputs the last i items of the list
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
