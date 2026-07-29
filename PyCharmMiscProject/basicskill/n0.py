#函数本节，函数是带名字的代码块，多次执行同一项任务时，只需调用即可
def greet_users(username):
    print(f"Hello,{username.title()}")
greet_users('jesse')
#注意实参与形参，在上述代码中，username无疑是形参，而我们调用函数时，则将实参信息放在圆括号内
#位置实参
def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster','harry')
#确保实参与形参的顺序一致
#关键字实参,直接在实参中奖名称同值相关联起来，如此便无需考虑调用函数时的实参顺序
def describe_pets(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster',pet_name='harry')
#编写函数时，可以给每个形参指定默认值。在调用函数中给形参提供了实参时，python将使用指定的实参值，否则默认
def describe_pet(pet_name,animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name = 'willie')
#使用默认值的时候必须先在形参列表中列出未给默认值的形参，再列出有默认值的实参
#函数并非总是直接显示输出，它还可以处理一些数据，并返回一个或一组值，可使用return语句
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)
#让实参编程可选的，可使用默认值来让实参变成可选的,下为例
def get_formatted_name(first_name,middle_name,last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi','lee','hooker')
print(musician)
#但是并不是每个人都有middle_name，那么这个时候我们可以给其设置一个空白的默认值
def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('john','hooker','lee')
print(musician)
#在函数体重，检查是否提供了中间名。python将非空字符串解读为true，因此若函数调用中提供了中间名，则true
def build_person(first_name,last_name,age = None):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix',age=27)
print(musician)
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
def make_album(artist,album,num_songs=None):
    album_info = {'artist':artist,'album':album}
    if num_songs:
        album_info[num_songs] = num_songs
    return album_info
albums = []
while True:
    artist = input('Enter artist: (press q to quit)')
    if artist == 'q':
        break
    album = input('Enter album: (press q to quit)')
    if album == 'q':
        break
    album_info = make_album(artist,album)
    albums.append(album_info)
for album in albums:
    print(album)