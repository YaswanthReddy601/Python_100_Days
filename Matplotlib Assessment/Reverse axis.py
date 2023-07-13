import pandas
import matplotlib.pyplot as mpl

df = pandas.read_csv("data.csv")

names = [name for name in df.name]
ages = [age for age in df.age]

# mpl.title("normal")
# mpl.plot(names,ages)

mpl.title("reverse")
mpl.scatter(names, ages)
mpl.ylim(10,40)
mpl.plot(names, ages, label="ages")
mpl.legend()
#gca() gets the currect axis instanceon the current figure
mpl.gca().invert_yaxis()
mpl.gca().invert_xaxis()
mpl.show()







