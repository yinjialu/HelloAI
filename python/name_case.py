name = 'jialu'
message = f"Hello {name.title()}, would you like to learn some Python today?"

print(message)

print(name.lower())
print(name.upper())
print(name.title())

famous_person = ' \tAlbert Einstein \n'
talk = f'{famous_person.strip()} once said, "A person who never made a mistake never tried anything new."'
print(talk)

talk = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(talk)

filename = 'python_notes.py'
print(filename.removesuffix('.py'))