from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224
TIMER_LABEL = "Timer"
TIMER_TEXT = "00:00"


# ---------------------------- TIMER RESET ------------------------------- #
def update_check_marks():
    marks = ""
    no_of_work_sessions = int(reps / 2)

    for _ in range(no_of_work_sessions):
        marks += CHECK
    check_marks.config(text=marks)


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="Long break!", fg=GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text="Short break!", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        title.config(text="Keep working.", fg=RED)


def reset_timer():
    global reps, timer

    window.after_cancel(timer)
    title.config(text=TIMER_LABEL, fg=GREEN)
    canvas.itemconfig(timer_text, text=TIMER_TEXT)
    reps = 0
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer

    count_min = int(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        update_check_marks()


# ---------------------------- UI SETUP ------------------------------- #
reps = 0
timer = None

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

title = Label(text=TIMER_LABEL, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"), padx=30, pady=30)
title.grid(row=0, column=1)

canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=tomato_img)
timer_text = canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2 + 18, text=TIMER_TEXT, fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

check_marks = Label(bg=YELLOW, fg=GREEN, padx=30, pady=30, font=(FONT_NAME, 40))
check_marks.grid(row=3, column=1)


window.mainloop()
