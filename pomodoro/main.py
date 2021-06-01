from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=500)
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, foreground=GREEN)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if 0 <= count_sec < 10:
        count_sec = f"0{count_sec}"
    if 0 <= count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        if reps % 2 == 0:
            mark = check_marks["text"]
            check_marks.config(text=f"{mark}✓")


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="BREAK", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="WORK", fg=RED)


start = Button(text="Start", width=7, command=start_timer)
start.grid(column=0, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
check_marks.grid(column=1, row=3)


def timer_reset():
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0


reset = Button(text="Reset", width=7, command=timer_reset)
reset.grid(column=2, row=2)


window.mainloop()