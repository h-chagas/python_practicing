# Build a program that asks the user name. 
## If it has 4 letters or less, reply "Your name is short". 
## If it has between 5 and 6 letters, reply "Your name has a normal length". 
## And if the name has more than 6 letters, reply "Your name is long"

name = input("What\'s your name? ")
name_length = len(name)

if name:
    if name_length  <= 4:
        print("Your name is short.")
    elif name_length >= 5 and name_length <= 6:
        print("Your name has a normal length.")
    else:
        print("You have a long name!")
else:
    print("You should type a name. Try again!")