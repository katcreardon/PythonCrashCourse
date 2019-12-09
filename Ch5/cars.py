cars = ['audi', 'bmw', 'subaru', 'toyota']

#loop first checks if the current value of car is 'bmw'
#if it is, it is printed in uppercase instead of titlecase
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())