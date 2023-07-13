import pandas

student_data = {
    "Student" : ["ram", "shyam", "Bheem"],
    "marks" : [50, 51, 98]
}

student_data_frame = pandas.DataFrame(student_data)

# for (index, rows) in student_data_frame.items():
#     print(rows)

for (index, rows) in student_data_frame.iterrows():
    print(rows)

# {index : row for index,row in student_data_frame.iterrows()}

