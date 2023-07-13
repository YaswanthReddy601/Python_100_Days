import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for x in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for x in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for x in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORDS ------------------------------- #
def add_data():
    website = website_entry.get()
    passsword = password_entry.get()
    email = user_entry.get()
    new_data = {
        website :{
        "email" : email,
        "password" : passsword
        }
    }

    #Checking if user provided data or not
    if website == "":
        alert = messagebox.showwarning(title="Error", message="Enter the website name")
    elif passsword == "":
        alert = messagebox.showwarning(title="Error", message="Enter the password")
    elif email == "":
        alert = messagebox.showwarning(title="Error", message="Enter Username or Email ")
    else:
        #Adding data to the Json file
        try:
            with open("data.json", "r") as data_file:
                old_data = json.load(data_file)
        except FileNotFoundError:
            print("there is no file with the given name and now the file is created created")
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            old_data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(old_data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#By this code we may get FileNotFound Error
        # with open("data.json", "r") as data:
        #     x = json.load(data)
        #     x.update(new_data)
        # with open("data.json", "w") as data:
        #     json.dump(x, data, indent=4)
        #     website_entry.delete(0, END)
        #     password_entry.delete(0, END)

#Dealing with text file
        # conformation = messagebox.askokcancel(title="Conformation", message=f"email: {email} and password: {passsword}. \n Click ok to save")
        #
        # if conformation:
        #     with open("All_Passwords.txt", "a") as ap:
        #         ap.write(f"{website}|{email}|{passsword}\n")
        #         website_entry.delete(0, END)
        #         password_entry.delete(0, END)
# ---------------------------- Search ------------------------------- #
def search():
    website = website_entry.get()
    with open("data.json", "r") as file:
        x = json.load(file)
        # Checking if the given data is the JSON or not
        if website in x:
            messagebox.showinfo(title =f"{website}", message=f"{x[website]['email']}\n{x[website]['password']}")
        else:
            messagebox.showinfo(title =f"{website}", message="No data found")
# ---------------------------- Deleting ------------------------------- #
def delete():
    website = website_entry.get()
    with open("data.json", "r") as file:
        x = json.load(file)
        # print(x[website][""])
        if website in x:
            for y in x.items():
                if y == website:
                    print("abcd")
                    messagebox.showinfo(title =f"{website}", message=f"{x[website]['email']}\n{x[website]['password']}\n got deleted")
                    del x[f"{website}"]
                    with open("data.json", "w") as data_file:
                        json.dump(x, data_file, indent=4)
                    # break
        else:
            messagebox.showinfo(title =f"{website}", message="No data found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# Creating window
window.title("Password Manager")
window.config(padx=50, pady=20)

#Adding image
canvas = Canvas(width=200, height=220)
photo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = photo)
canvas.grid(row=0, column=1)

#Labels
website_lable = Label(text="Website:", font=("Areal"))
website_lable.grid(row=1, column=0)

user_lable = Label(text="Email/UserName:", font=("Areal"))
user_lable.grid(row=2, column=0)

password_lable = Label(text="Password:", font=("Areal"))
password_lable.grid(row=3, column=0)

#Entries
website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(row=1, column=1)

user_entry = Entry(width=50)
user_entry.insert(0,"yaswanthreddy601@gmail.com")
user_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

#Buttons
generate_button = Button(text="Generate Password", command= generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add",width=42, command=add_data)
add_button.grid(row=4,column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

delete_button = Button(text="Delete", width=42, command=delete)
delete_button.grid(row=5, column=1, columnspan=2)

window.mainloop()