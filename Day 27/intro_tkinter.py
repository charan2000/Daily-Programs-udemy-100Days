import tkinter
from tkinter import *

window = tkinter.Tk()
window.minsize(width=500, height=300)
window.title("Program")
window.config(padx=40, pady=40)


def button_clicked():
    my_label.config(text=input.get(), font=("Monaco", 20))
    my_label.grid(column=1, row=1)


# Label
my_label = tkinter.Label(text="I am a Label", font=("Monaco", 20, "bold"))
my_label.grid(column=1, row=1)
my_label.config(padx=20, pady=20)
# my_label.pack(expand=True)

# Entry
input = Entry(width=15)
input.grid(column=4, row=4)

# Button
button = tkinter.Button(text="Click here", command=button_clicked)
button.grid(column=2, row=2)

# Another Button:
button2 = tkinter.Button(text="New Button")
button2.grid(column=3, row=1)

window.mainloop()



