# import sqlite3
#
#
# db = sqlite3.connect("books_collection.db")
# curser = db.cursor()
#
# curser.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varcar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# # curser.execute("INSERT INTO books VALUES (1, 'Harry Potter', 'Rowling', '9.3')")
# # db.commit()
#
# curser.execute("INSERT INTO books VALUES(2, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()



import matplotlib.pyplot as mpl

mpl.barh(["Cat","Dogs","Snakes"],[10, 13, 16],[1,5,7], align="center")

mpl.show()


import matplotlib.pyplot as plt

# # Pass the x and y cordinates of the bars to the
# # function. The label argument gives a label to the data.
# plt.barh(["Cats","Dogs","Goldfish","Snakes","Turtles"],
# [5,2,7,8,2], align='center', label="Data 1")
# # plt.legend()
#
# # plt.ylabel('Pets')
# # plt.xlabel('Popularity')
# # plt.title('Popularity of pets in the neighbourhood')
#
# plt.show()