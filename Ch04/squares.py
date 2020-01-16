# Computes x^2 for each x in the range
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# More concise code
squares_2 = []
for value in range(1,11):
    squares_2.append(value**2)

print(squares_2)

# List comprehension
squares_3 = [value**2 for value in range(1,11)]
print(squares_3)
