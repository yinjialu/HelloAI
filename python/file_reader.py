from pathlib import Path

path = Path("pi_digits.txt")
contents = path.read_text()
print(contents)

path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

for line in contents.splitlines():
    print(line)
    
for line in contents.splitlines():
    print(line.replace('Python', 'C'))
    
path.write_text('I love programming in Python!')

name = input("Enter your name: ")
path = Path('guest.txt')
path.write_text(name)

# 编写一个 while 循环，提示用户输入其名字。收
# 集用户输入的所有名字，将其写入 guest_book.txt，并确保这个文件中
# 的每条记录都独占一行。

path = Path('guest_book.txt')
guests = []
while True:
    name = input("Enter your name: ")
    if name == 'q':
        break
    else:
        print(f"Hello, {name}!")
        guests.append(name)
        print('guests:', guests)
        guest_str = ''
        for name in guests:
            guest_str += name + '\n'
        print(guest_str)
        path.write_text(guest_str)