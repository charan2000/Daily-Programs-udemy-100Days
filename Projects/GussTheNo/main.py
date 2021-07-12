import random as rdm
import art
def validation(guessedNo,level):
    flag = True
    counter=0
    if level == "easy":
        counter = 10
    elif level == "hard":
        counter=5
    while counter!=0:
        guessingNo = int(input(f"You have {counter} chances left\n Enter a number to guess: "))
        if guessedNo>guessingNo:
            print("Its too Low: ")
            counter-=1
        elif guessedNo<guessingNo:
            print("Its too High: ")
            counter-=1
        else:
            print(f"Yay U guessed the Correct No. {guessedNo}")
            print(art.won)
            exit()

print(art.logo)
guessedNo = rdm.randint(1,100)
#print(guessedNo)
level = input("Choose a difficulty: Easy / Hard").lower()
validation(guessedNo,level)




