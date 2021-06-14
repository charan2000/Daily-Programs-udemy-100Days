import random as rdm

side = rdm.randint(0,1)
def head_tail(side):
    if side == 1:
        return "Heads"
    else:
        return "Tails"

print(head_tail(side))