# To check if the Python interpreter passed in a condition, I can create a FLAG
# To create a flag, I can create a variable and give a NONE value

flag = None
condition = True

if condition:
    print("Condition is true")
    flag = True
else:
    print("Condition is not true")

# If the condition is True, the flag will become True
# If the condition is not True, the flag will still be None

if flag is None:
    print("The Python interpreter DIDN'T PASS in the if condition above")
    
if flag is not None:
    print("The Python interpreter PASSED in the if condition above")
    