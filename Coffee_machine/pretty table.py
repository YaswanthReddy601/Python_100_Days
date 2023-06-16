from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Name",["ram","janaki"])
table.add_column("gender",["male","female"])

table.align = "l"

print(table)