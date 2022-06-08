

sentance = "What is the airspeed velocity of unladen swallow?"

list_of_words = sentance.split()

word_count = {word: len(word) for word in list_of_words}

print(word_count)