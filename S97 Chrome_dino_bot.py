import time

import pyautogui as auto


while(True):
    screenshot= auto.screenshot()
    screen_color_white= screenshot.getpixel((101, 150))

    t1= screenshot.getpixel((330, 670))
    t3= screenshot.getpixel((523, 651))
    t2= screenshot.getpixel((510, 645))

    b1= screenshot.getpixel((315, 554))
    # b2= screenshot.getpixel((475, 554))

    if screen_color_white[0]==255:
        if t1[0] != 255 or t3[0] != 255 or t2[0] != 255:
            auto.press("space")
        elif b1[0] != 255:
            auto.keyDown("Down")
            auto.keyUp("Up")
    else:
        if t1[0] != 0 or t3[0] != 0:
            print("xx")
            auto.press("space")




# Code to get the x and y co-ordinates
# while(True):
#     time.sleep(2)
#     print(auto.position())


