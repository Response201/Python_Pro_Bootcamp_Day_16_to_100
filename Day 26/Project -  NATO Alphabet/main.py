import time
import pandas
from turtle import Screen,textinput
from text import TextWriter

writer_text = TextWriter()
screen = Screen()
screen.setup(700,500)
screen.title("")

data=pandas.read_csv("nato_phonetic_alphabet.csv")

run=True

# Frågar användaren efter ett ord att koda
def question():
    return textinput(f"NATO phonetic alphabet", "Type a word:" )


while run:

    text_input = question()

    # Om ordet är 11 tecken eller längre, fråga om nytt ord
    if text_input and len(text_input) >= 11:
        text_input = question()

    if text_input:
        # Konvertera text_input till stora bokstäver, skapa dictionary med NATO-koder och lista med koder för varje bokstav
        text = list(text_input.upper())
        alpha_code = {row.letter: row.code for (index, row) in data.iterrows()}
        alpha_word = [alpha_code[letter] for letter in text]


        # Skriv ut kodat ord
        writer_text.text_code = alpha_word
        writer_text.write_text()

        # Vänta 2 sek, rensa text och ställ ny fråga
        time.sleep(2)
        writer_text.clear()
    else:
        run =False
        screen.bye()

screen.mainloop()