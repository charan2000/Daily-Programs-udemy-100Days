import random as rdm

input_names = input("Enter the Names of the Business people: ").split(", ")

rdm_num = rdm.randint(0,len(input_names))
print(f"{input_names[rdm_num]} has to pay for the meal this time!!!")