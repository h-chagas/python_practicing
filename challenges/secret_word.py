### Secret word

# The programmer will choose a secret word  hardcoded
# The user will guess the word typing letter by letter
# - if the word doesn't have the letter, say to user;
# - if the letter is correct, reveal to user which position it is in the word, e.g, L*V*
# Display the number of tries every try


####### My Solution  - to run my solution, just uncomment lines 12-41 at once and comment out the tutor solution

# encrypt_word = '****'
# in_list_enc = list(encrypt_word)
# count = 0

# while True:
#     secret_word = "love"
#     letter = input("Guess a letter: ")

#     if letter in secret_word:
#         in_list = list(secret_word)
        
#         letter_in_list_index = in_list.index(letter)
#         in_list_enc[letter_in_list_index] = letter
        
#         print(in_list_enc)
#         print(f"{letter} is in {secret_word}")
#         count += 1
#         print(f"You tried {count} time(s)")
        
#         enc_word_str = "".join(str(element) for element in in_list_enc)
        
#         if enc_word_str == secret_word:
#             print(f"You win. The word is {enc_word_str}.")
#             break
            
        
#     else:
#         print(f"{letter} is not in {secret_word}")
#         count += 1
#         print(f"You tried {count} time(s)")


# Tutor solution


print("Guess the word!")
guessed_letters = ""
secret_word = 'house'
count = 0

while True:
    typed_letter = input("Type a letter: ")
    
    if len(typed_letter) > 1:
        print("Type only 1 letter")
        continue
    
    if typed_letter in secret_word:
        guessed_letters += typed_letter
    
    final_word = ''
    for x in secret_word:
        if x in guessed_letters:
            final_word += x
        else:
            final_word += "*"
    count+=1
    print(f"You try {count} time(s)")
    print(final_word)
    
    if secret_word == final_word:
        print(f"Well done. YOUR WIN! The secret word is {final_word}.")
    