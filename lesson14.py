'''
try / except introduction

just an introduction - this is not used like that - just to introduction purpose
'''

num_str = input('I will double your number. Type a number: ')

try:
    num_float = float(num_str)
    print('FLOAT: ', num_float)
    print(f'Your number {num_float} doubled is {num_float * 2:.2f}')
except:
    print('This is NOT a number!')
