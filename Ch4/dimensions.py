dimensions = (200, 50)
# New values cannot be assigned to an item in a tuple
# dimensions[0] = 250
print(dimensions[0])
print(dimensions[1])

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# Overwriting the entire variable is allowed
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
