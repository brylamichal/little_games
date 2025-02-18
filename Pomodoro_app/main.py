import tkinter
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def restart_timer():
    global reps
    reps = 0

    start_but.configure(state="normal")
    restart_but.configure(state="disabled")

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    ticks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    restart_but.configure(state="normal")
    start_but.configure(state="disabled")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count % 60}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        show_window()
        marks = ""
        for i in range(floor(reps/2)):
            marks += "✔"
        ticks.config(text=marks)

# ---------------------------- SHOW UP ------------------------------- #


def show_window():
    if window.state() == 'withdrawn':
        window.deiconify()
    elif window.state() == 'iconic':
        window.deiconify()
    window.lift()

# ---------------------------- UI SETUP ------------------------------- #


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title("Pomodoro")
    window.config(padx=25, pady=10, bg=YELLOW)
    window.resizable(width=False, height=False)
    window.attributes("-topmost", True)

    title = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
    title.grid(row=0, column=1)

    canvas = tkinter.Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
    tomato_img = tkinter.PhotoImage(file="tomato.png")
    canvas.create_image(100, 110, image=tomato_img)
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(row=1, column=1)

    start_but = tkinter.Button(text="Start", font=(FONT_NAME, 12), highlightthickness=0, command=start_timer)
    start_but.grid(row=2, column=0)

    restart_but = tkinter.Button(text="Restart", font=(FONT_NAME, 12), highlightthickness=0, command=restart_timer)
    restart_but.grid(row=2, column=2)
    restart_but.configure(state="disabled")

    ticks = tkinter.Label(bg=YELLOW, fg=GREEN, font=25)
    ticks.grid(row=3, column=1)

    window.mainloop()
