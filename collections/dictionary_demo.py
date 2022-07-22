# 1st way of populating key-value pairs
person_1 = {}
person_1['first_name'] = "Mark"
person_1['last_name'] = "Perez"
person_1['age'] = 27

# 2nd way of pre-populating key-value pairs
person_2 = {
            'first_name': 'Trinity',
            'last_name': 'Ruelas',
            'age': '24',
            'phone_number': {'mobile': '000-000-0011', 'work': '000-000-0022'}}

#print(person_1) # prints the first person's info
#print(person_2) # prints the second person's info

print(person_1['first_name'])   # Mark
print(person_1['last_name'])    # Perez
print(person_1['age'])  # 27

print(person_2['first_name'])   # Trinity
print(person_2['last_name'])    # Ruelas
print(person_2['age'])  # 24
print(person_2['phone_number']['mobile'])   # 000-000-0011
print(person_2['phone_number']['work'])     # 000-000-0022

my_tuple = (10, 15, 20)
my_dict_1 = {
    my_tuple: 'Here is my tuple'
}

print(my_dict_1[(10, 15, 20)])

# Iterating over a dictionary
for j in person_1:
    print(f"{j}: {person_1[j]}")

# person_1.items() -> [('first_name', 'Mark'), ('last_name', 'Perez'), ('age': 27)]
# .items() returns a list containing a tuple for the key-value pair
for j, v in person_1.items():
    print(f"{j}: {v}")

# .keys() returns a list of keys
for key in person_1.keys():
    print(key)

# .values() returns a list of all the values
for value in person_1.values():
    print(value)

# .pop() to remove a specified key-value pair for a given key
a = person_1.pop('age')
print(a)
print(person_1)

print(person_1['first_name'])
print(person_1.get('first_name'))

# print(person_1['favorite_hobby'])  # KeyError because the favorite_hobby key does not exist
print(person_1.get('favorite_hobby'))  # None
print(person_1.get('favorite_hobby', 'No favorite hobby'))  # Second argument will be returned if no key favorite_hobby
# is found