def display_message():
    print("I am learning python")
    
display_message()

def favorite_book(title):
    print("One of my favorite books is " + title)
favorite_book("Alice in Wonderland")

def make_shirt(size, text='I love Python'):
    print("The size of the shirt is " + size + " and the text is " + text)
    
make_shirt("Large", "Hello World")
make_shirt(text="Hello World", size="Large")
make_shirt("large")
make_shirt("Small", "Hello World")
make_shirt('Extra Large', 'Hello World')

def describe_city(city, country='China'):
    print(city + " is in " + country)
    
describe_city("Beijing")
describe_city("Shanghai")
describe_city("Tokyo", "Japan")

def make_album(artist, title, tracks=''):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

# while True:
#     print("\nPlease tell me the name of the artist and the title of the album.")
#     print("(enter 'q' at any time to quit)")
    
#     artist = input("Artist: ")
#     if artist == 'q':
#         break
#     title = input("Title: ")
#     if title == 'q':
#         break
    
#     album = make_album(artist, title)
#     print(album)

def show_magicians(magicians):
    for magician in magicians:
        print(magician)
        
magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print("Sending message: " + current_message)
        sent_messages.append(current_message)
        
messages = ['Hello', 'Hi', 'How are you?']
sent_messages = []
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)

def sandwich(*items):
    print("The sandwich has the following items:")
    for item in items:
        print("- " + item)
sandwich('lettuce', 'tomato', 'cheese')

def use_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

print(use_profile('Albert', 'Einstein', location='Princeton', field='physics'))
print(use_profile('Marie', 'Curie', location='Paris', field='chemistry'))

def make_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car
print(make_shirt('subaru', 'outback', color='blue', tow_package=True))