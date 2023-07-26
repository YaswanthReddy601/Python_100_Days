import PyPDF2
import pyttsx3

#opening the file in read-binary mode
file= open("xyz.pdf","rb")
#reading the file
file_data= PyPDF2.PdfReader(file)

#initializing the pyttsx3 module
speaker= pyttsx3.init()
#getting the voices
voices= speaker.getProperty("voices")
#setting the required voice
speaker.setProperty("voice", voices[1].id)

# extracting each page text and giving it to pyttsx3 module to read
for page_number in range(0,len(file_data.pages)):
    each_page= file_data.pages[page_number]
    page_text= each_page.extract_text()
    speaker.say(page_text)
    print("page "+str(page_number+1)+" started")
    speaker.runAndWait()#starts the speach and blocks the app untill the engine finish the speaking
    print("page "+str(page_number+1)+" completed")



