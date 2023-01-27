from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    checkMark.config(text="")
    global reps
    reps=1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    work_sec = WORK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    if reps%8 == 0:
        countdown(long_break_sec)
        title.config(text='Break', fg=RED)
    elif reps%2 == 0:
        countdown(short_break_sec)
        title.config(text='Break', fg=PINK)
    else:
        countdown(work_sec)
        title.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    sec = count%60
    if sec < 10:
        sec = f"0{sec}"
    count = f"{count//60}:{sec}"
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        global timer
        timer = window.after(1000,countdown, count-1)
    else:
        startTimer()
        global reps
        checkMark.config(text='✔️'*reps//2)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Noice")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text='Timer', fg=GREEN, bg=YELLOW ,font=(FONT_NAME, 50, ))
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photoImage = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=photoImage)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start = Button(text='start', highlightthickness=0, command=startTimer)
start.grid(column=0, row=2)
reset = Button(text='reset', highlightthickness=0,command=reset_timer)
reset.grid(column=2, row=2)

checkMark = Label(fg=GREEN, bg=YELLOW)
checkMark.grid(column=1, row=3)

window.mainloop()