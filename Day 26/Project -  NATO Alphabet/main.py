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

    text_input = textinput(f"NATO phonetic alphabet", "Type a word:" )

    # Om Cancel trycks → skicka tillbaks None
    if text_input is None:
        return None
    # Om ordet är längre än 10 tecken eller innehåller 0 tecken -> fråga om nytt ord
    if  len(text_input) >= 11 or  len(text_input) <= 0:
          return ""

    return text_input


while run:

    text_input = question()

    #  None -> avsluta programmet och loopen
    if text_input is None:
        run = False
        screen.bye()
        break

    if text_input:

        # Konvertera text_input till stora bokstäver, skapa dictionary med NATO-koder och lista med koder för varje bokstav
        text = list(text_input.upper())
        alpha_code = {row.letter: row.code for (index, row) in data.iterrows()}

        try:

            alpha_word = [alpha_code[letter] for letter in text]

        except KeyError:

            print("Sorry, only letters in the alphabet please")

        else:

            # Skriv ut kodat ord
            writer_text.text_code = alpha_word
            writer_text.write_text()

            # Vänta 2 sek, rensa text och ställ ny fråga
            time.sleep(2)
            writer_text.clear()


else:

        screen.bye()

screen.mainloop()