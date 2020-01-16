motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles_2 = []
motorcycles_2.append('honda')
motorcycles_2.append('yamaha')
motorcycles_2.append('suzuki')
print(motorcycles_2)

motorcycles_2.insert(0, 'ducati')
print(motorcycles_2)

del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles_2.pop(0)
print(motorcycles_2)
print(popped_motorcycle)

motorcycles.remove('ducati')
print(motorcycles)
