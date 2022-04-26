import pandas as pd

data = pd.read_csv("squirrel_data.csv")

#print(data["Primary Fur Color"])
print(data["Primary Fur Color"].unique())

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels,cinnamon_squirrels,black_squirrels)
color_lst = (data["Primary Fur Color"].unique()).tolist()
print(color_lst[1])
sqrl_dict = {
    "Color":[color_lst[1],color_lst[2], color_lst[3]],
    "Count":[gray_squirrels,cinnamon_squirrels,black_squirrels]
}
data_sqrl_count = pd.DataFrame(sqrl_dict)
data_sqrl_count.to_csv("squirrel_count.csv")
