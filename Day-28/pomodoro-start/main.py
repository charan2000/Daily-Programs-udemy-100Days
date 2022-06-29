from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#6bbaaa"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_break = 60 * WORK_MIN
    short_break = 60 * SHORT_BREAK_MIN
    long_break = 60 * LONG_BREAK_MIN
    if reps % 8 == 0:
        count_down(long_break)
    elif reps%2 == 0:
        count_down(short_break)
    else:
        count_down(work_break)

    #count_down(25 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    cnt_mins = math.floor(count/60)
    cnt_sec = count % 60
    if cnt_sec < 10:
        cnt_sec = f"0{cnt_sec}"
    canvas.itemconfig(timer_text, text=f"{cnt_mins}:{cnt_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()
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
timer_text = canvas.create_text(125,125, text="00:00", fill="white", font=(FONT_NAME,25,"bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="start", highlightthickness=0, command=start_timer  )
start_button.grid(column=0,row=2)

reset_button = Button(text="reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()

