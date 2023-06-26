# #Creating and adding info
# with open("File.txt", "w") as file:
#     file.write("To [NAME]\n\nThe truth will set you free.")
#
# #Reading the file
# with open("File.txt", "r") as file:
#     data = file.read()
#     #Searching for a specific word
#     if "[NAME]" in data:
#         #Replacing the data
#         with open("File.txt", "a") as file:
#             data = data.replace("[NAME]","yaswanth")
#             print(data)


int p, q, r, s
Set p=1, q = 1for (each r from 0 to 2 )
	for (each s from -4 to -2 )
		p = p + 2if(p > r)
			Continue
		End if
		p = 1if(p > s)
			Jump out of the loop
		End if
	End for
End for
Print p + q
