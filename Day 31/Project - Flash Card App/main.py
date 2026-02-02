from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50,pady=50, background=BACKGROUND_COLOR)
window.title("Flash card")

# Läser in sparade ord, annars används originalfilen
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except:
    data = pd.read_csv("./data/french_words.csv")
    to_learn = data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")

# Aktuellt kort, sätts i get_question()
current_question = ""



def get_question():
    global current_question, flip_timer

    # Timer återställs vid ny fråga
    window.after_cancel(flip_timer)

    canvas_front.itemconfig(card_bg, image=photo_front)
    current_card = random.choice(to_learn)
    canvas_front.itemconfig(card_title, text="French", fill="black")
    canvas_front.itemconfig(card_question, text=current_card["French"], fill="black")
    current_question = current_card

    # Vänder kortet efter 3 sekunder
    flip_timer = window.after(3000, func=flip_card)




def flip_card():

    # Visar översättningen
    canvas_front.itemconfig(card_bg, image=photo_back)
    canvas_front.itemconfig(card_title, text="English", fill="white")
    canvas_front.itemconfig(card_question, text=current_question["English"], fill="white")

flip_timer = window.after(3000, func=flip_card)




def right_answer():

    # Tar bort ord som användaren kan och sparar filen
    to_learn.remove(current_question)
    learn=pd.DataFrame(to_learn)
    learn.to_csv("./data/words_to_learn.csv", index=False)

    # Ny fråga
    get_question()





        # ---------------------------- UI SETUP ------------------------------- #


# Card

canvas_front = Canvas( width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
photo_front= PhotoImage(file="images/card_front.png")
photo_back = PhotoImage(file="images/card_back.png")
card_bg =  canvas_front.create_image(400, 268, image=photo_front)
card_title = canvas_front.create_text(400, 150,text="Title", font=("Ariel", 40, "bold" ))
card_question = canvas_front.create_text(400, 270,text="question", font=("Ariel", 30, "italic" ))

canvas_front.grid(row=1, column=1, columnspan=2)

# Visar första frågan/kortet
get_question()




# Button - Right

btn_image_right= PhotoImage(file="./images/right.png")
button = Button(image=btn_image_right, highlightthickness=0, background=BACKGROUND_COLOR, borderwidth=0, command=right_answer)
button.grid(row=6, column=2, pady=20)



# Button - Wrong

btn_image_wrong= PhotoImage(file="./images/wrong.png")
button = Button(image=btn_image_wrong, highlightthickness=0, background=BACKGROUND_COLOR, borderwidth=0, command=get_question)
button.grid(row=6, column=1, pady=20)




window.mainloop()