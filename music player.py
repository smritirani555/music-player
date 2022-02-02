import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("playing")
    mixer.music.play()

def pausesong():
    songstatus.set("paused")
    mixer.music.pause()
def  stopsong():
    songstatus.set("stopped")
    mixer.music.stop()
def resumesong():
    songstatus.set("resuming")
    mixer.music.unpause()

root= Tk()
root.title("MUSIC PLAYER")

mixer.init()
songstatus= StringVar()
songstatus.set("choosing")

#playlist
playlist= Listbox(root,selectmode=SINGLE,bg="Blue",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\smrit\Music')
songs= os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn= Button(root,text= 'Play',command= playsong)
playbtn.config(font= ('arial',20),bg= 'Blue',fg= 'white',padx=7, pady=7)
playbtn.grid(row=1,column =1)

pausebtn= Button(root,text= 'Pause',command= pausesong)
pausebtn.config(font= ('arial',20),bg= 'Blue',fg= 'white',padx=7, pady=7)
pausebtn.grid(row=1,column =2)

stopbtn= Button(root,text= 'Stop',command= stopsong)
stopbtn.config(font= ('arial',20),bg= 'Blue',fg= 'white',padx=7, pady=7)
stopbtn.grid(row=1,column =3)

resumebtn= Button(root,text= 'Resume',command= resumesong)
resumebtn.config(font= ('arial',20),bg= 'Blue',fg= 'white',padx=7, pady=7)
resumebtn.grid(row=1,column =4)

mainloop()