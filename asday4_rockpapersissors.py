rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissors = '''
    _______+
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
game_picks = [rock,paper,scissors]
import random

def symbolforinput(n,game):
    if n == 1:
        return game[0]
    elif n == 2:
        return game[1]
    elif n == 3:
        return game[2]

def validation(user,system):
    if user >= 3 or system >= 3:
        print("Invalid input: ")
    else:
        if user == 1 and system == 2:
            return  "system wins"
        elif user == 2 and system == 3:
            return "system wins"
        elif user == 1 and system == 3:
            return "You won"
        elif (user == 1 and system == 1) or (user==2 and system==2) or (user==3 and system==3):
            return "It's a Draw"

print("Lets play Rock Paper Scissors:\n")
print("Enter 1 for Rock; \nEnter 2 for Paper; \nEnter 3 for Scissors;")
user_value= int(input())
comp_decison = random.randint(1,3)
print("You Choose ",symbolforinput(user_value,game_picks))
print("Computer Choose this: ",symbolforinput(comp_decison,game_picks))
print(validation(user_value,comp_decison))
 