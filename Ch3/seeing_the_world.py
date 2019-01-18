places = ['Quebec, Canada', 'Paris, France', 'Tokyo, Japan', 
            'San Diego, California', 'Cancun, Mexico']
print("The original list:")
print(places)
print("\n")

print("The alphabetical list:")
print(sorted(places))
print("\n")

print("The original list:")
print(places)
print("\n")

print("The reversed alphabetical list:")
print(sorted(places, reverse=True))
print("\n")

print("The reversed list:")
places.reverse()
print(places)
print("\n")

print("The unreversed list:")
places.reverse()
print(places)
print("\n")

print("The alphabetical list:")
places.sort()
print(places)
print("\n")

print("The reversed alphabetical list:")
places.sort(reverse=True)
print(places)
print("\n")
