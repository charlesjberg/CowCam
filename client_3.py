# Adopted from https://www.youtube.com/watch?v=bWwZF_zVf00

import io
import socket
import struct
from PIL import Image
from tkinter import *
import tkinter
from PIL import Image
from PIL import ImageTk
import os
import threading


width, height = 800, 600

serverName = '192.168.1.206'
serverPort = 8000

client_socket = socket.socket()
client_socket.connect(('192.168.1.206', 8000)) 


# Accept a single connection and make a file-like object out of it
connection = client_socket.makefile('rb')
global photoImg





def update_image():
        img = None
        #while True:
            # Read the length of the image as a 32-bit unsigned int. If the
            # length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        # if not image_len:
        #     break
            # Construct a stream to hold the image data and read the image
            # data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
            # Rewind the stream, open it as an image with PIL and do some
            # processing on it
        image_stream.seek(0)
        img = Image.open(image_stream)
        message = "Good"
        client_socket.sendto(message.encode(),
                    (serverName, serverPort))
        photoImg =  ImageTk.PhotoImage(img)
        print("Hello")
        return photoImg

# https://stackoverflow.com/questions/16366857/show-webcam-sequence-tkinter
def show_frame():
    imgtk = update_image()
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(50, show_frame)


def close_connection():
    message = "Done"
    client_socket.sendto(message.encode(),
                    (serverName, serverPort))
    # client_socket.shutdown()
    connection.close()
    messagebox.showwarning("showwarning", "Ending Stream and Closing Program")
    root.destroy()
#show_frame()
# showCow_button = Button(root, text="Show Cows!", command = show_frame, relief = "RAISED")
# showCow_button.place(x=10, y=500)
root = Tk()

root.geometry('800x800')
root.bind('<Escape>', lambda e: root.quit())
lmain = Label(root)
lmain.place(x=125, y= 110)
root.title("Cow Cam")

welcome_label = Label(root, text="Welcome to Cow Cam", font=("Arial Bold", 30))
welcome_label.place(x=200, y=10)
showCow_button = Button(root, text="Show Cows!", relief = "raised", command = show_frame, bg="green", fg="red", font=("Arial Bold", 15))
showCow_button.place(x=250, y=700)

stopCow_button = Button(root, text="Stop Stream", command = close_connection, relief = "raised", bg="red", fg="green", font=("Arial Bold", 15))
stopCow_button.place(x=450, y=700)

cow1 = Canvas(root, width = 200, height = 100)  
cow1.place(x=0,y=0)  
img = Image.open("C:/Users/CJ/Pictures/cow1.png")
img = img.resize((200,100), Image.ANTIALIAS) 
img = ImageTk.PhotoImage(img)
cow1.create_image(0, 0, anchor=NW, image=img) 

cow2 = Canvas(root, width = 200, height = 200)  
cow2.place(x=650,y=0)  
img2 = Image.open("C:/Users/CJ/Pictures/Zoro.png")
img2 = img2.resize((int(960/6) ,int(1280/6)), Image.ANTIALIAS) 
img2 = ImageTk.PhotoImage(img2)
cow2.create_image(0, 0, anchor=NW, image=img2)     
root.mainloop()
