enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'heatlh': 100,
    'name': 'Mudillo',
}

print(enemy)
print("Location X = " + str(enemy['loc_x']))
print("Location Y = " + str(enemy['loc_y']))
print("His name is: " + str(enemy['name']))

enemy['rank'] = 'Admiral'
print(enemy)

del enemy['rank']
print(enemy)
print("============================")
enemy['loc_x'] = enemy['loc_x'] + 40
enemy['heatlh'] = enemy['heatlh'] - 30
if enemy['heatlh'] < 80:
    enemy['color'] = 'yellow'

print(enemy)

print("===================")
print(enemy.keys())
print(enemy.values())