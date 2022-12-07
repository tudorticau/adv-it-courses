cities = ['New York', 'Chisinau', 'kiev', 'toronto']
print(cities)
print(len(cities))
print(cities[0])

print(cities[2].upper())

cities[2] = 'Tula'

print(cities)

cities.append('Leova')
print(cities)

cities.insert(2, 'Bucuresti')
print(cities)

del cities[2]
print(cities)

#cities.remove('leova')
print(cities)

deleted_city = cities.pop()
print("Deleted citiy is: " + deleted_city)
print(cities)


cities.reverse()
print(cities)