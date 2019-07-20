"""
Data type to store more than onve value in one variable name, in terms of key value pairs
Dictionary items are in brackets{} in key:value pairs, seperated with "," {'k1':'v1','k2':'v2'}
Dictionary is not sequenced, no indexing -> Mapping
"""

car = {'make': 'bmw', 'model': '550i', 'year': 2016}
print(car)

model = car['model']

print(model)

print(car['model'])

d = {}
print(d)

d['one'] = 1
d['two'] = 2
print(d)

sum_dict = d['two'] + 8
print(sum_dict)
print(d)
d['two'] = d['two'] + 8
print(d)




