my_foods = ['pizza', 'falafel', 'carrot cake']
# To copy a list, make a slice of the entire list by omitting first and second 
# indices
friend_foods = my_foods[:]

# This doesn't work:
# friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
# print(my_foods)
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
# print(friend_foods)
for food in friend_foods:
    print(food)
