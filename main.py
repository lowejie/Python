# # with open("weather_data.csv") as data_file:
# #      data = data_file.readlines()
# #      print(data)
# import pandas
# # import csv
# #
# # with open("../weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas as pd
#
# data = pd.read_csv("../weather_data.csv")
# print(type(data))
# # print(data['temp'])
#
# # data.to_dict = data.to_dict()
# # print(data.to_dict)
# #
# # # temp_list = data['temp'].to_list()
# # # print(len(temp_list))
# #
# # # avg_temp = sum(temp_list)/len(temp_list)
# # # print(avg_temp)
# #
# # print(data['temp'].mean())
# # print(data['temp'].max())
# #
# # #Get Data in Columns
# # # data['column_name']
# # print(data.condition)
#
# #Get Data in rows
# # print(data[data.day == 'Monday'])
# # print(data[data.temp == data.temp.max()])
# #
# # monday = data[data.day == 'Monday']
# # print(monday.condition)
# # print(monday.temp*9/5 + 32)
#
# #Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angel"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251011.csv")
squirrel_count = data.groupby(['Primary Fur Color']).size().reset_index(name='Count')
df = pd.DataFrame(squirrel_count)
df = df.rename(columns={'Primary Fur Color': 'Fur Color'})
print(df)