import matplotlib.pyplot as mpl
import pandas as pd

#REading data from CSV file
df = pd.read_csv("Data1.csv")

# getting data to x and y co-ordinates
x = [mark for mark in df.marks]
y = [name for name in df.names]

mpl.ylabel("Students")
mpl.xlabel("Marks")
mpl.xlim(0,100)
mpl.barh(y,x, label="Marks")
mpl.legend()

mpl.show()