# Find in the word

# Give a word
# Give one of few letters to check if there is (are) the letter(s) in the word given

word = input("Type a word: ")
letters = input("Type what you want to find: ")

if letters in word:
    print(f"{letters} is in {word}")
else:
    print(f"{letters} is not in {word}")

