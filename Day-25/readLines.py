# Reading the CSV data using with open
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
# But this works in inefficient way, So we use CSV lib

import csv
import pandas


with open("weather_data.csv") as d_file:
    data = csv.reader(d_file)
    temperature = []
    for row in data:
        temperature.append(row[1])

print(temperature)

