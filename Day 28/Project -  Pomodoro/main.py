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
LONG_BREAK_MIN =20
CHECKMARK = "✓"
reps = 0
window_timer = None
start = True

# ---------------------------- TIMER RESET ------------------------------- #

# Återställer timer, etiketter och checkmarks
def reset_timer():
    global reps, start
    reps = 0
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_count, text=f"00:00")
    checkmark.config(text="")
    window.after_cancel(window_timer)
    start=True


# ---------------------------- TIMER MECHANISM ------------------------------- #

# Startar Pomodoro om start är True
def start_pomodoro():
    global start
    if start:
        count_down()
        start = False



# Väljer rätt intervall (arbete eller paus) baserat på antal reps
def count_down():
    global reps
    reps += 1
    if reps % 8 == 0:
            timer(LONG_BREAK_MIN * 60)
            timer_label.config( text=f"Break", fg=RED)

    elif reps % 2 == 0:
            timer(SHORT_BREAK_MIN * 60)
            timer_label.config( text=f"Break", fg=PINK)

    else:
            timer(WORK_MIN * 60 )
            timer_label.config(text=f"Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# Räknar ner tiden sekund för sekund och uppdaterar canvas
def timer(work_time):
    global window_timer

    count_min = math.floor(work_time / 60)
    count_sec = work_time % 60

    # Säkerställer tvåsiffrig sekundvisning
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")


    if work_time > 0 :
       window_timer = window.after(1000, timer, work_time - 1)

    # Startar nästa intervall när work-time är 0
    else:

       count_down()

       # Lägger till checkmark efter varannan rep
       if reps % 2 == 0:
        checkmark_item = ""
        complete_work_sessions= math.floor(reps / 2)
        for i in range(complete_work_sessions):
            checkmark_item += CHECKMARK
        checkmark.config(text=f"{checkmark_item}")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.config(padx=50, pady=50, bg=YELLOW)
window.minsize(width=600, height=500)
window.title("Pomodoro")



# Konfigurera 12 kolumner/rows så att de tar lika mycket plats
for i in range(12):  # 0–11 = 12 kolumner
    window.grid_columnconfigure(i, weight=1)
    window.grid_rowconfigure(i, weight=1)


# Titel (Timer / Work / Break)
timer_label = Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"), justify="center")
timer_label.grid(column=6, row=0)

# Bild & Tid
canvas = Canvas(width=200, height=224,  bg=YELLOW, highlightthickness=0)
tomata_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image= tomata_img)

timer_count = canvas.create_text(100,135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=6, row=4)


# Start-knapp
start_button = Button(text="Start", bg="white", command=start_pomodoro)
start_button.grid(column=4, row=10)

# Reset-knapp
reset_button = Button(text="Reset", bg="white", command=reset_timer)
reset_button.grid(column=8, row=10)


# Checkmark
checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
checkmark.grid(column=6, row=11)



window.mainloop()