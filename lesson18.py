# WHILE loop
count = 0
while count <= 10:
    print(f"{count}")
    count += 1
print("Ended!")
print("")



# WHILE loop with break
count_ = 0
while count_ <= 10:
    print(f"{count_}")
    count_ += 1
    if count_ == 5:
        break
print("Ended in 4!")
print("")


# WHILE loop with continue
count1 = 0
while count1 <= 10:
    count1 += 1
    if count1 == 5:
        print(f"I won\'t show the {count1}")
        continue
    print(f"{count1}")
print("")



# Assignment Operators
# =   +=   -+   *=   /=   //=    **=    %=

number1 = 2
number1 += 1 # 3 
print(number1)

number2 = 2
number2 -= 1 # 1 
print(number2)


number3 = 2
number3 *= 2 # 4 
print(number3)


number4 = 2
number4 /= 2 # 1.0 
print(number4)


number5 = 2
number5 //= 2 # 1 
print(number5)

number6 = 2
number6 **= 4 # 16
print(number6)

number7 = 2
number7 %= 2 # 16
print(number7)


