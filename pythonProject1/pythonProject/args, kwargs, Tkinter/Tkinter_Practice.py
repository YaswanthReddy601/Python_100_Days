from tkinter import *

window = Tk()
window.title("Custome GUI Window")
window.minsize(width= 400, height= 300)

gui_lable = Label(text="First custome GUI")
# gui_lable.pack()#Uses to allocates the allocating or organize the widgets in blocks horizontally/ vertically
gui_lable.grid(row=0,column=0)

def buttop_clicked():
    # print("Button clicked")
    data = custom.get()
    gui_lable.config(text= data)
buttion = Button(text="Click", command=buttop_clicked)
# buttion.pack()
buttion.grid(row=1,column=1)

new_buttion = Button(text="New_Button")
new_buttion.grid(row=0, column=2)

custom = Entry(width=10)
# custom.pack()
custom.grid(row=2, column=3)



window.mainloop()