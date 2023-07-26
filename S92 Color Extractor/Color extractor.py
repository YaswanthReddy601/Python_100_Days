import cv2
import pandas as pd


image_path= "./colorpic.jpg"
#reading the image and resizing the image
img= cv2.imread(image_path)
img= cv2.resize(img, (800,600))

#reading the csv files of the colors
index= ["color", "color_name", "hex", "R", "G", "B"]
color_file= pd.read_csv("colors.csv", names=index)

clicked= False
r=g=b=x_pos=y_pos=0

#getting color name
def color_name(R, G, B):
    minimum= 10000
    clr_name=""
    for x in range(len(color_file)):
        #comparinthe the actual values and the values in the csv file
        d= abs(R - int(color_file.loc[x, "R"])) +abs(G - int(color_file.loc[x,"G"])) + abs(B - int(color_file.loc[x, "B"]))
        if d <= minimum:
            minimum= d
            #returning the minimun difference value row from csv file
            clr_name= color_file.loc[x,"color_name"]
    return clr_name

#function to get b, g, r values on where mouse double click
def clicker(event, x, y, flags, params):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, clicked
        clicked=True
        b, g, r = img[y, x]
        b= int(b)
        g= int(g)
        r= int(r)

#naming the window
cv2.namedWindow("image_window")
#setting mouse click event
cv2.setMouseCallback("image_window", clicker)

while True:
    #showing thee image in mindow named "image_window"
    cv2.imshow("image_window", img)
    #color detais shows topof the window
    if clicked:
        #creating the rectangel which starts at (20,20) axis and ends at (600,60) axis and -1 fills that color in entire rectangle
        cv2.rectangle(img, (20,20), (600,60), (b,g,r), -1 )
        #text to show inside the rectangle
        text= color_name(r, g, b)+" R="+str(r) +" G="+str(g) +" B="+str(b)
        #placing the text at (50, 50) axis with font size, font scale, color, thickness, linetype
        cv2.putText(img, text, (50,50), 2, 0.8, (255,255,255), 2, cv2.LINE_AA)
        if r+g+b >  600:
            #making the text color black when the box color is light color
            cv2.putText(img, text, (50, 50), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)

    if cv2.waitKey(10) & 0XFF == 27:
        break



