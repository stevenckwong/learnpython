#Examples on Dictionary

stuff = {'name':'Zed', 'age':39, 'height': 6*12+2}

print (stuff['name'])
print (stuff['age'])
print (stuff['height'])


states = {
    'New South Wales':'NSW',
    'South Australia':'SA',
    'Victoria':'VIC',
    'Queensland':'QLD',
    'Western Australia':'WA',
    'Tasmania':'TAS',
    'Northern Territory':'NT',
    'Australian Capital Territory':'ACT'
}

cities = {
    'NSW':'Sydney',
    'VIC':'Melbourne',
    'SA':'Adelaide'
}

cities['WA']='Perth'
cities['NT']='Darwin'

print ("-" * 10)
print ("NSW has " + cities['NSW'] + " as capital")
print (states['Victoria'] + " has " + cities[states['Victoria']] + " as capital")

print (f"The capital for Western Australia is {cities.get('WA')}")
print (f"The capital for Tasmania is {cities.get('TAS','Oops.. could not find Tasmania city')}")

print (f"Reverse lookup state of VIC is {states.get('VIC','Oops.. reverse lookup does not work')}")
print (f"The abbreviation for Victoria is {states.get('Victoria','You should not see this...')}")

del cities["VIC"]
print (f"The capital for VIC is {cities.get('VIC','Oops you just deleted the dictionary item for VIC')}")
