# Calculator with while

number1 = input("Type a number: ")
number2 = input("Type other number: ")
operator = input("What operation you'd like to do? (+ - * /) ")
operators = "+-*/"
ok = False

if number1.isnumeric() and number2.isnumeric():
        num1 = float(number1)
        num2 = float(number2)
        ok = True
else:
    print("Type numeric numbers")

while ok:
    result = 0
           
    if operator not in operators:
        print("Type a valid operator")
        break
        
    if operator == '+':
        result = num1 + num2
        print(f"{num1} {operator} {num2} = {result}")
    if operator == '-':
        result = num1 - num2
        print(f"{num1} {operator} {num2} = {result}")
    if operator == '*':
        result = num1 * num2
        print(f"{num1} {operator} {num2} = {result}")
    if operator == '/':
        result = num1 / num2
        print(f"{num1} {operator} {num2} = {result}")
    
    exit = input("Would you like to [e]xit? ")
    if exit.lower().startswith('e') == True:
        break
    num2 += 1.0
