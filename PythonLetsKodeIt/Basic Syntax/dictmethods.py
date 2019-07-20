"""
Dictionary Methods
"""

car = {'make': 'bmw', 'model': '550i', 'year': 2016}
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}

# list all the dictionary keys in cars
print(car.keys())
print(cars.keys())

# list all the dictionary values in cars
print(car.values())
print(cars.values())

# list complete key value pairs
print(car.items())
print(cars.items())

# copy the dictionary in the variable
car_copy = car.copy()
print(car_copy)

# clear the content of a dictionary
car_copy.clear()
print(car_copy)

# pop the key in a dictionary
print(car.pop('model'))
print(car)

