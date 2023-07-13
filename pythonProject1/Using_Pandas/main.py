import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
#
# dlist = data["temp"].tolist()
#
# #Normal from
# avg = f"{sum(dlist)/len(dlist):.2f}"
# print(avg)
#
# #Using pandas
# avg = data["temp"].mean()
# print(avg)
#
# H_Temp = data["temp"].max()
# print(data.temp.max())
#
# print(data[data.day == "Monday"])
# print("Highest temperature")
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# # print(monday.condition)
# # print(int(monday.temp) * 9/5 + 32)
#
#
#
# data_dict = {
#     "students" : ["ram","shyam"],
#     "marks" : [20,25]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("created_csv_with_pandas.csv")


records = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
count = 0
color_gray = records[records["Primary Fur Color"] == "Gray"]
color_black = records[records["Primary Fur Color"] == "Black"]
color_red = records[records["Primary Fur Color"] == "Cinnamon"]

print(len(color_gray))
print(len(color_black))
print(len(color_red))

data_dict = {
    "Fur Colors" : ["Gray", "Black", "Cinnamon"],
    "colors" : [len(color_gray), len(color_black), len(color_black)]
}

squrals = pandas.DataFrame(data_dict)

squrals.to_csv("squrals.csv")
print(squrals)