import sqlite3

#creating the database
db = sqlite3.connect("books_collection.db")
cursor = db.cursor()

cursor.execute("CREATE TABLE stu (id INTEGER PRIMARY KEY, studentName varchar(250) NOT NULL,  class varcar(250) NOT NULL, Score INTEGER NOT NULL)")


cursor.execute("INSERT INTO stu VALUES(501, 'Harry', '5th class', '93')")
db.commit()

