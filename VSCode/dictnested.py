"""
Nested Dictionary
d={'k1':{'nestk1':'nestv1','nestk2':'nestv2'}}
d['k1']['nestk1']
"""

cars={'bmw':{'model':'550i','year':'2016'},'benz' :{'model':'E350','year':2015}}
bmw_year = cars['bmw']['year']
print(bmw_year)
print(cars['benz']['model'])


