import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

IP_ADDRESS = "127.0.0.1"
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096

def musicWindow():
    window = Tk()
    window.title("Music Window")
    window.geometry("300x300")
    window.configure(bg="LightSkyBlue")

    selectLabel = Label(window, text="Select Song", bg="LightSkyBlue", font=("Calibri", 10))
    selectLabel.place(x=2, y=1)

    listBox = Listbox(window, height=10, width=39, activestyle="dotbox", bg="LightSkyBlue", borderwidth=2, font=("Calibri", 10))
    listBox.place(x=10, y=10)

    scrollbar1 = Scrollbar(listBox)
    scrollbar1.place(relheight=1, relx=1)
    scrollbar1.config(command=listBox.yview)

    playButton = Button(window, text="Play", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    playButton.place(x=30, y=200)

    stop = Button(window, text="Stop", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    stop.place(x=200, y=200)

    upload = Button(window, text="Upload", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    upload.place(x=30, y=250)

    download = Button(window, text="Download", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    download.place(x=200, y=250)

    infoLabel = Label(window, text="", fg="blue", font=("Calibri", 8))
    infoLabel.place(x=4, y=280)

    window.mainloop()

def setup():
    global PORT, SERVER, IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()

setup()