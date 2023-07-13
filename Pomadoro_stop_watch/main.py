import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rounds = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global rounds
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text= "00:00")
    timer_lable.config(text="Timer", fg=GREEN)
    tick.config(text="")
    rounds = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rounds
    rounds += 1
    work_sec= WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if rounds in [1,3,5,7]:
        timer_lable.config(text="Work",fg=GREEN)
        count_down(work_sec)
    elif rounds in [2,4,6]:
        timer_lable.config(text="Break",fg=PINK)
        count_down(short_break_sec)
    elif rounds == 8:
        timer_lable.config(text="Break",fg=RED)
        count_down(long_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minuts = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(canvas_text, text= f"{minuts}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        checks = ""
        sessions = math.floor(rounds/2)
        for x in range(sessions):
            checks += "✔"
            tick.config(text="", fg=GREEN, bg=YELLOW,  font=(FONT_NAME, 12, "bold"))

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomadoro watch")
window.config(padx=100, pady=50, bg =YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW)
photo = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image = photo)
canvas_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

timer_lable = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_lable.grid(row=0, column=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

tick =  Label(text="", fg=GREEN, bg=YELLOW,  font=(FONT_NAME, 12, "bold"))
tick.grid(row=3, column=1)

window.mainloop()
