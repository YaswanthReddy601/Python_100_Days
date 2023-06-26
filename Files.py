#Creating and adding info
with open("File.txt", "w") as file:
    file.write("To [NAME]\n\nThe truth will set you free.")

#Reading the file
with open("File.txt", "r") as file:
    data = file.read()
    #Searching for a specific word
    if "[NAME]" in data:
        #Replacing the data
        with open("File.txt", "a") as file:
            data = data.replace("[NAME]","yaswanth")
            print(data)

