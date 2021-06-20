import random

## Creating a word list ##
word_list = ["Berry","Jerry","Ferry","dragonfruit","mobile","laptop","building","jewellery","knowledge"]
choosen_word = random.choice(word_list)
print(choosen_word)
user_word=""
display=""
for i in choosen_word:
    display+="_"
for i in choosen_word:
    input_letter = input("Enter a letter that might fit in the blanks: \n").lower()
    
    if input_letter in choosen_word:
        user_word += input_letter
    else:
        print("Sry the letter u choose is not fit for the Word :(\n Try again \n")





if choosen_word == user_word:
    print("You Won")
else:print("You Lost")

