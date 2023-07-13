# with open("weather_data.csv") as wd:
#     data = wd.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as wd:
#     data = csv.reader(wd)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row [1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["condition"])
