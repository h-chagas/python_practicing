# f-strings formatting

# s - string
# d and i - float
# f - float
#  x and X 

# > - left
# < - right
# ^ - center 
# + or -

var1 = 'abc'
print(f'{var1: >10}') # complete the number of the characters of the var1 variable on the left, until complete 10 characters
print(f'{var1: <10}') # complete the number of the characters of the var1 variable on the right, until complete 10 characters
print(f'{var1:0^10}') # center var1 and add as many zeros as possible until ten characters
print(f'{100.75565214561:.2f}') # limit float number until two characters. (rounds up or down)
print(f'{1060.7:,.2f}') # add a comma (,) to separate thousands