import tkinter

window = tkinter.Tk()
window.minsize(300,200)
window.config(padx=50, pady=10)


button = tkinter.Button(text = "Butom")
# button.pack(side="right")
# button.place(x=10,y=20)
button.grid(row=0,column=0)

radio1 = tkinter.Radiobutton(text="choose1")
# radio1.pack(side="left")
# radio1.place(x=50, y= 90)
radio1.grid(row=1,column=1)
radio1.config(padx=100, pady=20)

check = tkinter.Checkbutton(text="check")
# check.pack()
# check.place(x=100, y=50)
check.grid(row=2, column=3)

entry = tkinter.Entry(width=10)
entry.grid(row=0, column=2)

window.mainloop()