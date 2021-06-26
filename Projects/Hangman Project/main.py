import random
import words
import animation

print(animation.logo)
choosen_word = random.choice(words.word_list)
print(choosen_word)
word_len = len(choosen_word)
print(word_len)
display = []

for i in range(word_len):
    display += "_"
lives = 6
end_game = False
while not end_game:
    guess = input("Enter a letter: ").lower()
    for i in range(word_len):
        input_letter = choosen_word[i]
        if input_letter == guess:
            display[i] = input_letter
    print(display)
    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You Lost")

    print(animation.stages[lives])

    if "_" not in display:
        end_game = True
        print("You Win")
