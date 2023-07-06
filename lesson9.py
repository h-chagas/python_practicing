# > greater than
# >= greater or equal to 

# < less than
# <= less or equal to

# == equals to 
# != different to 

greater_than = 2 > 1
less_than = 1 < 2
is_greater_or_equals = 3 >= 4
is_less_or_equals = 6 <= 6

# Exercise:

first_number = input("Type a number: ")
second_number = input("Type another number: ")

if first_number > second_number:
    print(f"The {first_number=} is greater than the {second_number=}")
elif first_number == second_number:
    print(f"The {first_number=} and second number={second_number=} are equal")
else:
    print(f"The {second_number=} is greater than the {first_number=}")