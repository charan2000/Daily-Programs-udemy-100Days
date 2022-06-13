import tkinter


window = tkinter.Tk()
window.minsize(600, 500)

label = tkinter.Label(text="Hello", font=("Monaco",20))
label.pack()

button = tkinter.Button(text="Click Me", command='')
button.pack()

entry = tkinter.Entry(width=19)
entry.pack()

text = tkinter.Text()

window.mainloop()




