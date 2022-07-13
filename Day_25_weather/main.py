# import csv
#
#
#
# with open("./Weather_data - Sheet1.csv") as data_file:
#     data = csv.reader(data_file)
#     tempratures = []
#     for row in data:
#         if row[1]!= "temp":
#             tempratures.append(int(row[1]))
#     print(tempratures)

import pandas

data = pandas.read_csv("./Weather_data - Sheet1.csv")
# print (data["temp"])
#print(type(data["temp]))

data_dict = data.to_dict()
#print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)
#
# def find_avg(list):
#     total = 0
#     x = sum(list)
#     print(x)
#     average_x = x / len(list)
#     print(average_x)
#
# find_avg(temp_list)

#print(data["temp"].mean())
#print(data["temp"].max())

"""Squirrel data"""

data_squirrel = pandas.read_csv("./2018_CP_Squirrel_Data.csv")

#Dataframe.loc[Dataframe['Primary Fur Color'] == "Gray"] # color options (Gray, Cinnamon, Black

gray_squirrel_count = len(data_squirrel[data_squirrel["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data_squirrel[data_squirrel["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data_squirrel[data_squirrel["Primary Fur Color"] == "Black"])


print(gray_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
