import serial as ser
import time
import tkinter as tk
import cv2
import sys

BUTTONWIDTH = 20
BUTTONHEIGHT = 2
VIDEO_WIDTH, VIDEO_HEIGHT = 800, 600

#send data over serial bus, and print incoming data
def send_data(letter):
    ser.write(letter)
    #change the bit number to 16 if you remove the print statements in the arduino code
    print(ser.read(26)) 

m=tk.Tk()  #main window
m.title('Science Team Drill Controls')  #window title

#connect to arduino
try:
    ser = ser.Serial("COM5", 9600)
    time.sleep(0.1)
except ser.serialutil.SerialException:
    print("Arduino not connected")
    sys.exit()

# Define a video capture object 
vid = cv2.VideoCapture(0) 

# Set the width and height 
vid.set(cv2.CAP_PROP_FRAME_WIDTH, VIDEO_WIDTH) 
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, VIDEO_HEIGHT)

# Bind the app with Escape keyboard to 
# quit app whenever pressed 
m.bind('<Escape>', lambda e: m.quit()) 

# Create a label and display it on app 
label_widget = tk.Label(m) 

#Drill 1 Up
drill_1_up = tk.Button(m, text='Drill 1 Up', 
                       width=BUTTONWIDTH, 
                       height= BUTTONHEIGHT, 
                       bg="yellow",
                       font= ('Helvetica 20 bold'),
                       command= lambda:send_data(b's'))
#Drill 1 Down
drill_1_down = tk.Button(m, text='Drill 1 Down', 
                         width=BUTTONWIDTH,
                         height= BUTTONHEIGHT, 
                         bg="yellow",
                         font= ('Helvetica 20 bold'),
                         command= lambda:send_data(b'w'))
#Drill 1 FWD
drill_1_FWD = tk.Button(m, text='Drill 1 FWD', 
                        width=BUTTONWIDTH, 
                        height= BUTTONHEIGHT,
                        bg="yellow",
                        font= ('Helvetica 20 bold'),
                        command= lambda:send_data(b'd'))
#Drill 1 REV
drill_1_REV = tk.Button(m, text='Drill 1 REV', 
                        width=BUTTONWIDTH,
                        height= BUTTONHEIGHT, 
                        bg="yellow",
                        font= ('Helvetica 20 bold'),
                        command= lambda:send_data(b'a'))

#Drill 2 Down
drill_2_down = tk.Button(m, text='Drill 2 Down', 
                         width=BUTTONWIDTH,
                         height= BUTTONHEIGHT, 
                         bg="lightgreen",
                         font= ('Helvetica 20 bold'),
                         command= lambda:send_data(b'i'))
#Drill 2 Up
drill_2_up = tk.Button(m, text='Drill 2 Up', 
                       width=BUTTONWIDTH,
                       height= BUTTONHEIGHT, 
                       bg="lightgreen",
                       font= ('Helvetica 20 bold'),
                       command= lambda:send_data(b'k'))
#Drill 2 Clockwise
drill_2_CW = tk.Button(m, text='Drill 2 CW', 
                       width=BUTTONWIDTH,
                       height= BUTTONHEIGHT, 
                       bg="lightgreen",
                       font= ('Helvetica 20 bold'),
                       command= lambda:send_data(b'l'))
#Drill 2 Counter Clockwise
drill_2_CCW = tk.Button(m, text='Drill 2 CCW', 
                        width=BUTTONWIDTH,
                        height= BUTTONHEIGHT, 
                        bg="lightgreen",
                        font= ('Helvetica 20 bold'),
                        command= lambda:send_data(b'j'))

#Faster
faster = tk.Button(m, text='Faster', 
                   width=BUTTONWIDTH*2,
                   height= BUTTONHEIGHT, 
                   bg="lightblue",
                   font= ('Helvetica 20 bold'),
                   command= lambda:send_data(b'p'))
#Slower
slower = tk.Button(m, text='Slower', 
                   width=BUTTONWIDTH*2, 
                   height= BUTTONHEIGHT,
                   bg="lightblue",
                   font= ('Helvetica 20 bold'),
                   command= lambda:send_data(b'o'))

# Specify Grid
tk.Grid.columnconfigure(m, index = 0, weight = 1)
tk.Grid.rowconfigure(m, 0,weight = 1)
tk.Grid.columnconfigure(m, index = 1, weight = 1)
tk.Grid.rowconfigure(m, 1,weight = 1)
tk.Grid.columnconfigure(m, index = 2, weight = 1)
tk.Grid.rowconfigure(m, 2,weight = 1)
tk.Grid.columnconfigure(m, index = 3, weight = 1)

#place buttons
drill_1_up.grid(row=0,column=0,sticky="NSEW")
drill_1_down.grid(row=0,column=1,sticky="NSEW")
drill_1_FWD.grid(row=1,column=0,sticky="NSEW")
drill_1_REV.grid(row=1,column=1,sticky="NSEW")

drill_2_up.grid(row=0,column=2,sticky="NSEW")
drill_2_down.grid(row=0,column=3,sticky="NSEW")
drill_2_CW.grid(row=1,column=2,sticky="NSEW")
drill_2_CCW.grid(row=1,column=3,sticky="NSEW")

slower.grid(row=2,column=0,columnspan=2,sticky="NSEW")
faster.grid(row=2,column=2,columnspan=2,sticky="NSEW")

m.mainloop()
