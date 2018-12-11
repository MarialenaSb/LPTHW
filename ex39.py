states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print ('_' * 10)
print ("NY State has:", cities['NY'])
print ("OR State has:", cities['OR'])

print ('_' * 10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

print ('_' * 10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

#dict.items() returns a list containing the tuple for each key value pair
print('_' * 10)
for state, abbrev in states.items():
    print ("%s is abbreviated %s" %(state, abbrev))

print('_' * 10)
for abbrev, city in cities.items():
    print ("%s has the city %s" %(abbrev, city))

print('_' * 10)
for state, abbrev in states.items():
    print ("%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev]))

# dict.get('') returns the value of the specified key
print('_' * 10)
state = states.get('Texas', None)

if not state:
    print ("Sorry, no Texas")

city = cities.get('TX', 'Does Not Exist')
print ("The city for the state 'TX' is: %s" % city)

#practice

countries = {
    'Netherlands': 'NL',
    'Greece': 'GR',
    'Portugal': 'PT',
    'France': 'FR',
    'Romania': 'RO'
    }

cities = {
    'NL': 'Amsterdam, The Hague',
    'GR': 'Athens, Chalkis',
    'PT': 'Lisbon, Porto',
    'FR': 'Paris',
    'RO': 'Bucharest, Brasov'
}

print('.' * 20)
print("In NL I visited:", cities['NL'])
print ("In GR I have lived in:", cities['GR'])
print ("In Romania I visited:", cities[countries['Romania']])

print('.' * 20)
for country, abbrev in countries.items():
    print("%s is abbreviated %s" %(country, abbrev))

print('.' * 20)
for abbrev, city in cities.items():
    print("In %s Ihave visited the following cities: %s" %(abbrev, city))

print('.' * 20)
countries['Italy'] = 'IT'
cities['IT'] = 'Bologna'

print("I am planning to visit a new city, %s , which is in %s." % (cities['IT'], 'Italy'))

#dict.keys() returns a list containing the dictionary's keys
print("The countries I will have visited will be:", countries.keys())
#dict.values() returns a list of all the values in the dictionary
print ("These countries are abbreviated:",  countries.values())

#Dictionary methods
#cities.pop('NL')
#cities.popitem()
#del cities['GR']
#del cities
#cities.clear()

# In dictionaries I cannot add/remove an item at/from the specified index
