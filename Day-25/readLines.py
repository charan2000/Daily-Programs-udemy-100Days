# Reading the CSV data using with open
import pandas

with open("Datasets/weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
# But this works in inefficient way, So we use CSV lib

import csv
import pandas as pd


with open("Datasets/weather_data.csv") as d_file:
    data = csv.reader(d_file)
    temperature = []
    for row in data:
        temperature.append(row[1])
#print(temperature)

data_df = pd.read_csv("Datasets/weather_data.csv")
#print(data_df["temp"].max())
#(data_df.condition)
#print(data_df[data_df.day == "Monday"])

#print(data_df[data_df.temp == data_df.temp.max()])

### Convert the Mondays temp into farenhiet
print(((data_df[data_df.day == "Monday"].temp)*9/5 )+32)

### Creating new CSV file using Pandas method:
data_dict = {
    "students":["Amy","James","Angela"],
    "score":[76,44,32]
}
data_df_dict = pandas.DataFrame(data_dict)
data_df_dict.to_csv("new_data.csv")