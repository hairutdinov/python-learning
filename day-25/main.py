# with open("weather_data.csv") as file:
#     data = list(map(lambda l: l.strip(), file.readlines()))
#     print(data)


# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in list(data)[1:]:
#         temperatures.append(int(row[1]))
#
#     print(temperatures)


# import pandas
# data = pandas.read_csv("weather_data.csv")

# temperatures = data["temp"].to_list()
# print(temperatures)
# print(sum(temperatures) / len(temperatures))
# print(data["temp"].mean())

# data_dict = data.to_dict()
# print(data_dict)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# data_dict = {
#     "students": ["Amy", "James", "Angels"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
#
# data.to_csv("new_data.csv")

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

