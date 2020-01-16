cubes = [value**3 for value in range(1,11)]

for cube in cubes:
    print(cube)

print("The first three items in the list are:")
print(cubes[:3])

print("Three items from the middle of the list are:")
print(cubes[3:6])

print("The last three items in the list are:")
print(cubes[-3:])
