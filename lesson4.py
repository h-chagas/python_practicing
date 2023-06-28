#TYPE CONVERSION / TYPECASTING / COERCION

print(int("2") + 5)
print(float("-5") + 12)
print(float("2") + 2.3)
print(int(3.4) + 6)

print(bool("")) #False
print(bool(" ")) #True

print(1+ 'b') #TypeError: unsupported operand type(s) for +: 'int' and 'str'