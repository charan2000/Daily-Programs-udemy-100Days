import random

## Creating a word list ##
word_list = ["berry", "jerry", "ferry", "dragonfruit",
             "mobile", "laptop", "building", "jewellery", "knowledge"]
choosen_word = random.choice(word_list)
print(choosen_word)
display = []

for i in range(len(choosen_word)):
    display += "_"

end_game = False
while not end_game:
    guess = input("Enter a letter: ").lower()
    for i in range(len(choosen_word)):
        input_letter = choosen_word[i]
        if guess == input_letter:
            display[i] = guess
        else:
            print("Wrong letter")

    if "_" not in display:
        end_game = True
        print("You Won")

print(display)
