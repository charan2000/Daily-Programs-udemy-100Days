
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data)

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

dict_of_data = {row.letter: row.code for (index, row) in data.iterrows()}

#print(dict_of_data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Enter the Name: ").upper()

final_list = [dict_of_data[letter] for letter in name]

print(final_list)

