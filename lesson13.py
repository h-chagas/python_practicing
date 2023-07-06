#  String slice
var1 = 'abcdefghi'
var2 = 'Hello world!'

print(var1[2]) #c
print(var1[-1]) #i
print(var1[-2]) #h

print('')

print(var2[2:]) #llo world!
print(var2[:5]) #Hello
print(var2[1:]) #ello world!
print(var2[0:5]) #Hello
print(var2[6:11]) # the char of the index 11 is NOT included. In this case, the '!'     #world
print(var2[11]) #!

print('')

print(len(var1)) #9
print(len(var2)) #12

print('')

# starts from index : length to cover/finish at index : steps
print(var2[0:len(var2):2]) # Hlowrd
print(var2[::-1]) # !dlrow olleH       < INVERT STRING
print(var2[-1:-13:-1]) # !dlrow olleH       < INVERT STRING  (same; another approach)
print(var2[0:len(var2):3]) # Hlwl

print(var1[0:len(var1):2]) # acegi

