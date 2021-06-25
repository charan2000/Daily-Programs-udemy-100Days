import random
from typing import final
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

n_of_letters = int(input("How many letters do U need in ur password: \n"))
n_of_nums = int(input("How many Numbers do U need in ur password: \n"))
n_of_symbols = int(input("How many Symbols do U need in ur password: \n"))

final_password=""

for i in range(1,n_of_letters+1):
    final_password += random.choice(letters)

for i in range(1,(n_of_nums+1)):
    final_password += random.choice(numbers)

for i in range(1,(n_of_symbols+1)):
    final_password += random.choice(symbols)

#final_result = random.shuffle(final_password)
#print(final_result)








