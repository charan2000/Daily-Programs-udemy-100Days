from tkinter import *

window = Tk()
window.minsize(height=50, width=550)
window.title("Miles to Kilo-Meter Converter")

entry1 = Entry(width=20)
entry1.grid(column=1, row=0)

label = Label(text="Miles", font=('Monaco', 20))
label.grid(column=2, row=0)

label2 = Label(text="is equal to ", font=('Monaco', 20))
label2.grid(column=0, row=1)

label3 = Label(text="0", font=('Monaco', 20))
label3.grid(column=1, row=1)

label4 = Label(text=" Kilo-meters ", font=('Monaco', 20))
label4.grid(column=2, row=1)


def calculate():
    miles = entry1.get()
    km = 1.60934 * int(miles)
    label11 = Label(text=miles, font=('Monaco', 20,"bold"))
    label11.grid(column=0, row=0)
    label3.config(text=f"Approx {km}", font=('Monaco', 16, "bold"))
    label3.grid(column=1, row=1)


button1 = Button(text="Calculate", command=calculate)
button1.grid(column=1, row=2)

window.mainloop()
