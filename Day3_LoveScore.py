print("Welcome to the Love Calculator ")
name1 = input("What is ut name ?\n")
name2 = input("What is ur partners name ?\n")
combined_string = name1 + name2
lowerCased = combined_string.lower()
print(lowerCased)
### Score Calculator ###
def score_calculator(para):
    T = para.count("t")
    R = para.count("r")
    U = para.count("u")
    E = para.count("e")
    L = para.count("l")
    O = para.count("o")
    V = para.count("v")
    E = para.count("e")
    v1 = str(T+R+U+E)
    v2 = str(L+O+V+E)
    return (v1+v2)

def score_value(score):
    if score<10 or score>90:
        print("Your score is ",score,", you go together like coke and mentos." )
    elif score >= 40 and score<=50:
        print("Your score is ",score,", you are alright together.")
    else:
        print("Your score is ", score)

score = score_calculator(lowerCased)
score_value(int(score))