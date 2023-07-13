def outer():
    print("outer")
    def inner():
        print("inner")
    return inner

space = outer()
space()

def place():
    print("delhi")
#A function is an instance of the Object type.
out = place
out()

# ====================================
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()




def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper)

