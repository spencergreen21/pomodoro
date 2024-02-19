from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_button = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_clicked():
    window.after_cancel(timer_button)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_clicked():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        timer.config(text="Break", fg= RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def convert_time(count):
    count_min = math.floor(count / 60)
    return count_min


def convert_sec(count):
    count_second = count % 60
    if count_second == 0:
        count_second = "00"
    return count_second


def count_down(count):
    canvas.itemconfig(timer_text, text=f"{convert_time(count)}:{convert_sec(count)}")
    if count > 0:
        global timer_button
        timer_button = window.after(1000, count_down, count - 1)
    else:
        start_clicked()
        mark = ""
        for i in range(math.floor(reps / 2)):
            mark += "✓"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady=150, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer.grid(column=1, row=0)


startBtn = Button(text="Start", command=start_clicked, highlightthickness=0)
startBtn.grid(column=0, row=2)

resetBtn = Button(text="Reset", command=reset_clicked, highlightthickness=0)
resetBtn.grid(column=2, row=2)

checkmark = Label(bg=YELLOW, highlightthickness=0, fg=GREEN)
checkmark.grid(column=1, row=3)

window.mainloop()
# Event Driven, looping through GUI every millisecond
