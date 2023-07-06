user_name = input('What\'s your name? ')
user_age = input('How old are you? ')

if user_name == '' or user_age == '':
    print('Please, type both your name and age!')
else:
    print(f'Your name is {user_name}')
    print(f'Your name in reverse is {user_name[::-1]}')
    if ' ' in user_name:
        print('Your name has space in between!')
    else:
        print('Your name doesn\'t have spaces in between' )
    print(f'Your name has {len(user_name)} letters')
    print(f'The last letter of your name is {user_name[-1]}')