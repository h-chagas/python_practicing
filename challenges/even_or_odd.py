# Build a program that asks the user to type a int number, and you reply if it is even or odd
number = input("Type a integer number: ")

if number.isnumeric() and ("." not in number and "," not in number):
    num = int(number)
    if num % 2 == 0:
        print("Your number is even")
    else:
        print("Your name is odd")
else:
    print("Your should type an integer number. Please try again!")