# Basic interpolation - string

# s - string
# d and i - float
# f - float
#  x and X - hexadecimal (abddef0123456789) (ABCDEF0123456789)

name = 'Louis'
price = 190.090900909090

string = "Hi, %s" % name
print(string)
print("")

string1 = "%s, the price is £ %f" % (name, price)
print(string1)
print("")

string1 = "%s, the price is £ %.2f" % (name, price)
print(string1)
print("")

hex = "The hexadecimal of %d is %x" % (1500, 1500)
print(hex)
print("")

hex1 = "The hexadecimal of %d is %04x" % (1500, 1500)
print(hex1)
print("")

hex2 = "The hexadecimal of %d is %08X" % (1500, 1500)
print(hex2)
print("")