import json
filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='Latin-1')

player1 = {
    'PlayerName': 'Donald Trump',
    'Score': 345,
    'Awards': ["OR", "NV", "NY"]
}

player2 = {
    'PlayerName': 'Clinton Hillary',
    'Score': 346,
    'Awards': ["WT", "TX", "MI"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# ---- SAVE by JSON ----------

json.dump(myplayers, myfile)
myfile.close()

# ---- LOAD by JSON ----
myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)
for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    print("Player Awards N1 are: " + str(user['Awards'][0]))
    print("Player Awards N2 are: " + str(user['Awards'][1]))
    print("Player Awards N3 are: " + str(user['Awards'][2]))
    print("---------------------------------\n")

# --------------------------