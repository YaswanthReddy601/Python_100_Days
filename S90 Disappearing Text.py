from tkinter import Tk, Text


class Disappear():

    def __init__(self):
        self.window = Tk()  # Creating window
        self.text = Text(self.window)  # Text widget
        self.text.pack()  # Placing
        self.text.bind("<Key>", self.timer_bind)  # binding the timer_bind method with key

    def timer_bind(self, event=None):
        try:
            self.window.after_cancel(self.timer_clear)  # Stops/resets the .after methods(stops the calback)
        except AttributeError:
            pass
        self.timer_clear = self.window.after(5000, self.clear_text)  # after 5 seconds, calls clear_text

    def clear_text(self):
        self.text.delete(1.0, "end")  # clears the text

    def run(self):
        self.window.mainloop()  # holds the window


Disappear().run()

