import tkinter

window = tkinter.Tk()
window.minsize(width=300,height=200)
window.title("Mile to Km Calculator")

#Miles input
entry = tkinter.Entry(width=10)
entry.focus()
entry.insert(tkinter.END, string="0")
entry.grid(row=0, column=1)

#Miles lable
label = tkinter.Label(text="Miles", font="Areal 16")
label.grid(row=0, column=2)

#is equal lable
equal_lable = tkinter.Label(text="is equal to ", font="Areal 16")
equal_lable.grid(row=1,column=0)

#Km lable
km_lable = tkinter.Label(text="Km", font=("Areal 16"))
km_lable.grid(row=1, column=2)

#convereted kms
Km = tkinter.Label(text="0")
Km.grid(row=1, column=1)

kms = 0
#Conversion
def calculator():
    miles = int(entry.get())
    kms = round(miles * 1.609)
    Km.config(text=f"{kms}")

#Button to convert
button = tkinter.Button(text=" Calculate", command=calculator)
button.grid(row=2, column=1)







window.mainloop()
