from tkinter import *

#Creatingwindow
window = Tk()
window.minsize(500, 500)
window.title("Wedget Example")

#Lable
my_lable = Label(text= "This is Text", font=("calebre", 18))
my_lable.pack()

#button
def button_action():
    my_lable.config(text="Lable changed")

button = Button(text="Click", command=button_action)
button.pack()

#Entry
my_entry = Entry(width=15)
my_entry.focus()
my_entry.insert(END, string="Enter some data")
my_entry.pack()

#Text
text_box = Text(width=30, height=5)
# text_box.focus()
text_box.insert(END, "Enter the text data")
# print(text_box.get("1.0", END))
text_box.pack()

#Spin box
def spin_box():
    print(spin.get())

spin = Spinbox(from_=0, to=10, width=3, command= spin_box)
spin.pack()

#Scale box
def scale_box(value):
    print(value)

scale = Scale(from_=0, to=20, command=scale_box)
scale.pack()

def checkbutton_clicked():
    print(check_value.get())

check_value = IntVar()
check = Checkbutton(text= "check box", variable=check_value, command=checkbutton_clicked)
check.pack()

def radio_click():
    print(radia_state.get())

radia_state = IntVar()
rbutton1 = Radiobutton(text="Option1", value=1, variable=radia_state, command=radio_click)

rbutton2 = Radiobutton(text="Option2", value=2, variable=radia_state, command=radio_click)

rbutton1.pack()
rbutton2.pack()

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=5)
games = ["chess", "carroms", "snake"]
for game in games:
    listbox.insert(game.index(game),game)
listbox.bind("<<ListboxSelect>>",
listbox_used)
listbox.pack()

window.mainloop()