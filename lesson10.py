# Logic Operators


# and
print("")
print("and")
print("True and False ---> ", True and False)
print("True and 1 and 0 and 8 ---> ", True and 1 and 0 and 8)
print("0.0 and 1 and 0 and 8 ---> ", 0.0 and 1 and 0 and 8)



# not
print("")
print("not")
print("not True --> ", not True)
print("not False --> ", not False)


# in    not in
# strings are iterable
print("")
print("in  and  not in")
name = "Hugo"
print("variable name -->", name)
print("Is the letter H between letters of the variable name?", "H" in name)
print("Is the letter W between letters of the variable name?", "W" in name)
print("Is the letter W NOT between letters of the variable name?", "W" not in name)
print("Are the letters ugo between letters of the variable name?", "ugo" in name)



# or
print("")
print("or")
print("True or False --> ", True or False)
print("False or 0.0 or True --> ", False or 0.0 or True)
print("False or False or 0 or 'abc' --> ", False or False or 0 or 'abc')

e_or_E = input("Type e or E: ")
password = input("Type the correct password: ")
correct_password = "123"

if (e_or_E == "e" or e_or_E == "E") and password == correct_password:
    print("You're in!")
else:
    print("You're out!")














# None

# FALSY
# O     O.O      ""      False

# Truthy
#  