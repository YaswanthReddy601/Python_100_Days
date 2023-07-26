from tkinter import Tk, Label, Button, filedialog
from PIL import ImageTk, ImageDraw, ImageFont, Image

def upload_file():
    #selecting the image
    image_file= filedialog.askopenfilename(filetypes=[("Jpg Files", "*.jpg")])
    #opening the photo as image type
    draw = Image.open(image_file)
    #Opening the watermark image
    water_mark= Image.open("Z:\watermark.jpg")
    #applying the watermark
    draw.paste(water_mark)
    #showin the image
    draw.show()
    #saving the image
    # draw.save("name.jpg")




#Creating the object of thhe TK
window = Tk()
#Giving the title
window.title("WaterMarking")
#creating a label/ writing some text
name= Label(text="Upload Image to add Water mark", font="times")
name.grid(row=0, column=1)
#browsing the image
button1 = Button(text="Browse image", command=upload_file)
button1.grid(row=2, column=1)


#To keep the window alive
window.mainloop()






































# l = Label(image=img)
    # l.grid(row=3, column=1)
    # button2= Button(window, image=dra)
    # button2.grid(row=3, column=1)