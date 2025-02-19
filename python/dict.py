alien_0 = { 'color': 'green', 'points': 5 }
print(alien_0['color'])
print(alien_0['points'])

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(alien_0.get('abc', 'No value assigned.'))

person = {
    'first_name': 'zhang',
    'last_name': 'yi',
    'age': 18,
    'city': 'beijing',
}

for value in person.values():
    print(value)
    
for key, value in person.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    
languages = { 'zhang', 'python', 'yi', 'c', 'li', 'ruby' } # 集合和列表的区别是啥？
print(languages)

# print(languages[0])

for value in languages:
    print(value)
    
rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'yangtze': 'china',
}

for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}.")
    
persons = [ 'zhang', 'yi', 'lihua', 'beijing' ]

for person in persons:
    if person in favorite_languages.keys():
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take our poll!")
