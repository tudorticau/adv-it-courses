# Create dictionary
def create_record(name, telephone, address):
    """Create Reccord"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record

user1 = create_record("vasya", "+97251151", "Tunisia")
user2 = create_record("Petya", "+516516516", "Algeria")

print(user1)
print(user2)

def give_award(medal, *persons):
    """Give medal to persons"""
    for person in persons:
        print("Tovarisch " + person.title() + " se ofera medalie " + medal)

give_award("Za rabotu",  "vasya", "petya")
give_award("Za London", "petya", "alexander")