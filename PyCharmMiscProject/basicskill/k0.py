prompt = 'Please offer your pizza toppings!'
prompt += '\nif you enter quit we will end this fucking note. '
message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print('OK, we have added it.')
i = 'Please tell me your age.'
i += '\nWe will design the best way to buy tickets for you. '
age = ''
while age != 'quit':
    age = input(i)
    if age == 'quit':
        print('See you again!')
        break
    else:
        z = int(age)
        if z < 3:
            print('For free!')
        elif z > 12:
            print('Fifteen dollars please!')
        else:
            print('Ten dollars please!')
i = 'Please tell me your age.'
i += '\nWe will design the best way to buy tickets for you. '
age = ''
while True:
    age = input(i)
    if age == 'quit':
        print('See you again!')
        break
    else:
        z = int(age)
        if z < 3:
            print('For free!')
        elif z > 12:
            print('Fifteen dollars please!')
        else:
            print('Ten dollars please!')

i = 'Please tell me your age.'
i += '\nWe will design the best way to buy tickets for you. '
active = True
while active:
    age = input(i)
    if age == 'quit':
        active = False
    else:
        z = int(age)
        if z < 3:
            print('For free!')
        elif z > 12:
            print('Fifteen dollars please!')
        else:
            print('Ten dollars please!')

