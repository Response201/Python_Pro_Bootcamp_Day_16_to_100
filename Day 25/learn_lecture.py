
#import csv
#with open("weather_data.cvs") as file:
#    data = csv.reader(file)
#    only_days = []
#    for row in data:
#        if "day" not in row:
#            day = row[0]
#            temp = int(row[1])
#            weather = row[2]
#            only_days.append([day, temp, weather])
#
#    print(only_days)




"""  PANDAS """

import pandas
data = pandas.read_csv("weather_data.cvs")

#Get columns - 2 ways
#print(data["temp"])
#print(data.temp)



#new_list = data["temp"].to_list()
#average_temperature = round(sum(new_list) / len(new_list), 2)
#print(average_temperature)
# or
#print(round(data["temp"].mean(), 2))



# Find row in dataset
#print(data[data["temp"] == data["temp"].max()]  )
# Get temp for selected day
#print(data[data["temp"] == data["temp"].max()]["temp"]  )



#monday_temp_celsius = data[data["day"] == "Monday"]["temp"]
#monday_temp_fahrenheit  = ( monday_temp_celsius * 1.8) + 32
#print(monday_temp_fahrenheit)



# Skip row
#skip_rows = pandas.read_csv("weather_data.cvs", skiprows = 1)
#print(skip_rows)



# Create dataframe / save as csv-file

#data_dict = {
#    "students":["David", "Molly", "Jess"],
#    "scores":[76,55,60]
#}
#new_dataframe =pandas.DataFrame(data_dict)
#new_dataframe.to_csv("new_file.csv")
#print(new_dataframe)