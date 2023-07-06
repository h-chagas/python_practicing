# Input function (collect data from user)
# first_name = input("What's your first name? ")
# surname = input("What's your surname? ")
# print(f'Your full name is {first_name} {surname}')

number1 = input("Type a number: ")
number2 = input("Type other number: ")

#BEST PRACTICE - Check if the inputs are numbers, then make them numbers (int or float)
#DON'T make them numbers in the same line of the inputs above. The user can type a letter, then the program will crash

if (number1.isnumeric() and number2.isnumeric()):
    n1 = int(number1)
    n2 = int(number2)
else: 
    print("One of your inputs aren't a number") 

result = n1 + n2

print(type(result))
print(f"The sum of these two numbers is {result}")
    
