from tkinter import *

window = Tk()
window.title("Example Widget")
window.minsize(600, 500)

label = Label(text="Hello", font=("Monaco",20))
label.pack()

def action():
    print("Clicked the top Button")

button = Button(text="Click Me", command=action)
button.pack()

entry = Entry(width=19)
entry.insert(END, "E-Mail address")
entry.pack()

text = Text(height=7, width=34)
text.pack()
text.insert(END, "Example of Multi-line Text entry")

def spin_box():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10,width=10, command=spin_box )
spinbox.pack()

def value_scaled(val):
    print(val)

scale = Scale(from_=10, to=50, command=value_scaled)
scale.pack()

def check_function():
    print(check_state.get())

check_state = IntVar()
check_button = Checkbutton(text="True / False", variable=check_state, command=check_function)
check_button.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()



