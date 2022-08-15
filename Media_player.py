import pygame
from pygame import mixer
from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
from PIL import ImageTk, Image


# tkinter window
root = Tk()
root.title('Music player project')
root['background'] = '#000000'
root.geometry('1500x600')


# functions

def open_folder():
    playlist.delete(0,END)
    path = filedialog.askdirectory()
    os.chdir(path)
    songs = os.listdir(path)
    for s in songs:
        if'.mp3' in s:
             playlist.insert(END, s)
            # else:
            #     messagebox.showinfo('Wait!!', 'no audio files found')
            #     break


def playsong():
	try:
		currentsong = playlist.get(ACTIVE)
		mixer.music.load(currentsong)
		mixer.music.play()
		songstatus.set("Playing  "+currentsong)
	except:
		messagebox.showinfo('wait','select a directory')


def pausesong():
    try:
        mixer.music.pause()
        songstatus.set("Paused")
    except:
        messagebox.showinfo('wait','select a directory')

def stopsong():
    try:
        mixer.music.stop()
        songstatus.set("Stopped")
    except:
        messagebox.showinfo('wait','select a directory')


def resumesong():
    try:
        mixer.music.unpause()
        songstatus.set("Resuming")
    except:
        messagebox.showinfo('wait','select a directory')



   
   



# pygame mixer to play music


mixer.init()
songstatus = StringVar()  # this is us to display the current song status
songstatus.set("choosing")



#Create an object of Scrollbar widget
s = Scrollbar()

#Create a horizontal scrollbar
scrollbar = Scrollbar(root, orient= 'vertical')
scrollbar.pack(side= RIGHT, fill= BOTH)


playlist = Listbox(root, selectmode=SINGLE, bg="#2b2928",
                   fg="white", font=('arial', 15), height=180, width=30)
# playlist.grid(columnspan=7)
playlist.pack(side= LEFT, fill= BOTH)


playlist.config(yscrollcommand= scrollbar.set)

#Configure the scrollbar
scrollbar.config(command= playlist.yview)


resumeIMAGE = Image.open("resume.png")
resumeIMAGE_RESIZE = resumeIMAGE.resize((50, 50))
resumeIMAGE_RESIZE_BUTTON = ImageTk.PhotoImage(resumeIMAGE_RESIZE)


fileIMAGE = Image.open("files.png")
fileIMAGE_RESIZE = fileIMAGE.resize((50, 50))
fileIMAGE_RESIZE_BUTTON = ImageTk.PhotoImage(fileIMAGE_RESIZE)


playIMAGE = Image.open("play.png")
playIMAGE_RESIZE = playIMAGE.resize((50, 50))
playIMAGE_RESIZE_BUTTON = ImageTk.PhotoImage(playIMAGE_RESIZE)


pauseIMAGE = Image.open("pause.png")
pauseIMAGE_RESIZE = pauseIMAGE.resize((50, 50))
pauseIMAGE_RESIZE_BUTTON = ImageTk.PhotoImage(pauseIMAGE_RESIZE)


stopIMAGE = Image.open("stop.png")
stopIMAGE_RESIZE = stopIMAGE.resize((50, 50))
stopIMAGE_RESIZE_BUTTON = ImageTk.PhotoImage(stopIMAGE_RESIZE)


playbtn = Button(root, text="play", image=playIMAGE_RESIZE_BUTTON,
                 borderwidth=0, command=playsong)
playbtn.config(font=('arial', 20), bg="#000000",
               fg="white",)
playbtn.place(relx=0.6, rely=0.9)


filebt = Button(root, text="file", image=fileIMAGE_RESIZE_BUTTON,
                borderwidth=0, bg="#000000", command=open_folder)
filebt.config(font=('arial', 20),
              fg="white",)
filebt.place(relx=0.7, rely=0.9)


pausebtn = Button(root, text="Pause", image=pauseIMAGE_RESIZE_BUTTON,
                  borderwidth=0, bg="#000000", command=pausesong)
pausebtn.config(font=('arial', 20),
                fg="white", padx=7, pady=7)
pausebtn.place(relx=0.5, rely=0.9)

stopbtn = Button(root, text="Stop", image=stopIMAGE_RESIZE_BUTTON,
                 borderwidth=0, bg="#000000", command=stopsong)
stopbtn.config(font=('arial', 20),
               fg="white", padx=7, pady=7)
stopbtn.place(relx=0.4, rely=0.9)

Resumebtn = Button(root, text="Resume", image=resumeIMAGE_RESIZE_BUTTON,
                   borderwidth=0, bg="#000000", command=resumesong)
Resumebtn.config(font=('arial', 20),
                 fg="white", padx=7, pady=7)
Resumebtn.place(relx=0.3, rely=0.9)

label = Label(root, textvariable=songstatus, relief=RAISED,
              height=3, width=70,font=("Arial", 12), bg='#2b2928', fg='#ffffff')
label.place(relx=0.4, rely=0.1)


root.mainloop()
