from turtle import Turtle, Screen

jack = Turtle()
scr = Screen()

def move_forwards():
    jack.forward(10)

def move_backwords():
    jack.backward(10)

def move_left():
    angle = jack.left(10)

def move_right():
    angle = jack.right(10)

def clear_screen():
    jack.clear()
    jack.penup()
    jack.home()

scr.listen()
scr.onkey(move_forwards,"6")
scr.onkey(move_backwords,"4")
scr.onkey(move_left,"8")
scr.onkey(move_right,"2")
scr.onkey(clear_screen,"5")
scr.exitonclick()