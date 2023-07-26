from tkinter import Tk, Canvas, Button, Label, Text, Entry, END, StringVar

MIN= 1
TEXT="Once upon a time there was an old mother pig who had three little pigs and not enough food to feed them.\n " \
     "So when they were old enough, she sent them out into the world to seek their fortunes.\n" \
     "The first little pig was very lazy. He didn't want to work at all and he built his house out of straw.\n" \
     "The second little pig worked a little bit harder but he was somewhat lazy too and he built his house out of sticks.\n" \
     "Then, they sang and danced and played together the rest of the day. The third little pig worked hard all day and built his house with bricks.\n" \
     "It was a sturdy house complete with a fine fireplace and chimney.It looked like it could withstand the strongest winds.\n" \
     "The next day, a wolf happened to pass by the lane where the three little pigs lived and he saw the straw house, and he smelled the pig inside.\n" \
     "He thought the pig would make a mighty fine meal and his mouth began to water."


#timer
def timer():
    window.after(60000, result)

#Verifing the data
def result():
    entered_data= data.get()
    data_set= entered_data.split()

    given_set= TEXT.split()
    crt_count=0
    wrng_count=0
    for x in range(0,len(data_set)):
        if given_set[x] == data_set[x]:
            crt_count+=1
        else:
            wrng_count+=1

    #destroys the window
    window.destroy()
    window.title("Speed Test Result")
    #creating a new window and giving the result
    result= Label(text=f"You typed {crt_count} words correctly and {wrng_count} words are spell mistaken.", font=("Aerial",18,"italic"))
    result.grid(row=3, column=1)





#Creating the window
window= Tk()
#Title of the window
window.title("Typing Speed Test")
#Size of the window
window.geometry("1300x500")

#Giving the text to type
text= Label(text=TEXT,font=("Aerial",14,"bold"))
text.grid(row=0, column=1)

# variable to store the data we typed in the entry wedget
data= StringVar()
#entry widget
text_area = Entry(window, textvariable=data, width=50)
text_area.grid(row=1, column=1)

#button, starts the timmer
start_button= Button(text="Start", command=timer)
start_button.grid(row=2, column=1)

#Giving the importent note points
x= Label(window, text="You have 1 minute to type the above short story type as much as you can.\n"
                      "Note2: Please Click Start before typing the words.\n"
                      "Note3: Do not press enter button.", font=("Aerial",12))
x.grid(row=4, column=1)

window.mainloop()


