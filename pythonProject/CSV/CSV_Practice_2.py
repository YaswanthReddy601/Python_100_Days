import csv

file = open("makeup_new.csv", encoding="utf-8")

file1 = csv.reader(file)

file2 = list(file1)
# print(file2)

# for x in file2:
#     print(x)

file4 = open("csv_practice1.csv", mode="a" , newline ="")
file5 = csv.writer(file4, delimiter=" ")
file5.writerow("Yaswanth")
# file4 = open("csv_practice1.csv")
# file6 = csv.reader(file4)
# file7 = list(file6)
# print(file7)


file4.close()



