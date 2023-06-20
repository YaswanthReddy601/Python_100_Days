import csv

ex = open("example.csv", encoding= "utf-8")
data = csv.reader(ex)

x = list(data)
# for y in x[:10]:
#     print(y)

# full_names = []
# for y in x[:10]:
#     full_names.append(y[1]+" "+y[2])
# print(full_names)


# emails = []
# for y in x[:10]:
#     emails.append(y[3])
# print(emails)


file = open("csv_practice.csv", mode="w", newline="")
csv = csv.writer(file,delimiter= " ")
csv.writerow("Hello World")

file.close()


