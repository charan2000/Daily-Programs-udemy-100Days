import tkinter
from tkinter import *

window = tkinter.Tk()

window.minsize(width=500, height=300)
window.title("Program")


#Label


my_label = tkinter.Label(text="I am a Label", font=("Monaco", 20, "bold"))
my_label.pack()
my_label.pack(expand=True)

def button_clicked():
    my_label.config(text=input.get(), font=("Monaco",20))
    my_label.pack(expand=True)

# Entry

input = Entry(width=15)
input.pack(expand=True)

# Button

button = tkinter.Button(text="Click here", command=button_clicked)
button.pack()

window.mainloop()