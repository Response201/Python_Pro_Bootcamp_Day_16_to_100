import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_unique_colors = data[data["Primary Fur Color"].notna()]["Primary Fur Color"].unique()
squirrel_color_count = data["Primary Fur Color"].value_counts().tolist()

data_dict = {
   "Fur color":squirrel_unique_colors,
    "Count":squirrel_color_count
}

pandas.DataFrame(data_dict).to_csv("squirrels.csv")