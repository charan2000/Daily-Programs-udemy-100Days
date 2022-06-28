

# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#6bbaaa"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title(" Pomodaro ")
window.config(pady=50, padx=100, bg=YELLOW)
canvas = Canvas(width=240, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

label1 = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
label1.grid(column=1,row=0)

label2 = Label(text="✔", font=(FONT_NAME, 30, "bold"),  fg=GREEN, bg=YELLOW)
label2.grid(column=1, row=3)

canvas.create_image(120, 112, image=tomato_img)
canvas.create_text(125,125, text="00:00", fill="white", font=(FONT_NAME,25,"bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="s tart")
start_button.grid(column=0,row=2)

reset_button = Button(text="reset")
reset_button.grid(column=2, row=2)

window.mainloop()

