# with open("weather.csv", "r") as file:
#     ls = file.readlines()
# print(ls)

# import csv

# with open("weather.csv", "r") as file:
#     data = csv.reader(file, delimiter=";")
#     # for line in data:
#     #     print(line)
#
#     headers = next(data)
#     rows = [row for row in data]
#     temperatures = [int(row[1]) for row in rows]
#     print(temperatures)

import pandas as pd

data = pd.read_csv("weather.csv", delimiter=";")
# print(data)
#
# dic = data.to_dict()
# print(dic)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# print(sum(temp_list)/len(temp_list))
# print(data['temp'].mean())
#
# print(data['temp'].max())
#
# print(data.temp)

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# print(data[data.day == 'Monday'].temp * 9/5 + 32)

# data_dict = {
#     "students": ["Ödön", "Tádé", "Bendegúz"],
#     "scores": [76, 12, 0]
# }

# scores = pd.DataFrame(data_dict)
# print(scores)

# with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250212.csv") as file:
#     squirrel_data = pd.read_csv(file, delimiter=',')
#     # print(list(squirrel_data))
#     print(squirrel_data['Primary Fur Color'].value_counts())
