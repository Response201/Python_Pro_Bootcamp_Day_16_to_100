from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

window = Tk()
window.minsize(width=425, height=400)
window.maxsize(width=425, height=400)
window.config(padx=50,pady=10)
window.title("Password")

for i in range(12):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Genererar ett slumpmässigt lösenord (12 tecken)
def generate_password():
    password_entery.delete(0, END)
    digits = "123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    special = "!@#$%&"
    all_chars = digits + letters + special
    random_password =  "".join([random.choice(all_chars) for item in range(12)])
    password_entery.insert(END,  random_password)

    # Kopierar lösenord till clipboard
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# Sparar webbsida, email och lösenord i csv-fil och återställer webbsida- och lösenordsfält
def save_password():
    website = website_entery.get().title()
    email = email_entery.get()
    password = password_entery.get()

    # Kontrollerar så att inga fält är tomma
    if not website or not email or not password:
        message_box("Please don't leave any fields empty!")
        return

    # Frågar användaren om uppgifterna ska sparas
    save = messagebox.askokcancel(title=website, message=f"These are the details entered:\n\n Website: {website}\n Email: {email}\n Password: {password}\n\n It is ok to save?")

    if save:
        new_data = {website: {"email": email, "password": password}}
        try:
            with open("data.json", mode="r") as file:
                # Hämtar fil
                find_data = json.load(file)

        # Om filen inte finns skapas en ny fil och en post med infon
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)

        else:
                # Om webbplatsen redan finns i filen -> uppdateras info
                # Om webbplatsen inte finns -> läggs all info till som en ny post
                find_data.update(new_data)

                # Sparar
                with open("data.json", mode="w") as file:
                    json.dump(find_data, file, indent=4)

        finally:

            # Rensar inputfält för webbplats och lösenord
            website_entery.delete(0, END)
            website_entery.insert(END, "Website")
            password_entery.delete(0, END)

            # Genererar ett nytt lösenord direkt
            generate_password()





# ---------------------------- SEARCH PASSWORD ------------------------------- #



def search_password():
    website = website_entery.get().title()
    try:
        # Läser in all sparad data
        with open("data.json", mode="r") as file:
            data = json.load(file)

    except FileNotFoundError:
        message_box("No saved data found for this website")


    else:

        if website in data:

            # Tar ut info för webbsida
            website_data = data[website]

            # Fyller i lösenordet- & email-fälten
            password_entery.delete(0,END)
            password_entery.insert(END, website_data["password"])
            email_entery.delete(0, END)
            email_entery.insert(END, website_data["email"] )

            # Kopierar lösenord till clipboard
            pyperclip.copy(website_data["password"])

        else:

            # Om webbsidan inte finns i filen eller om input-fältet för "website" är tomt
            if not website_entery.get():
                message_box("Please enter a website!")

            else:
                message_box("No saved data found for this website")


# ---------------------------- UI SETUP ------------------------------- #

# Logo-bild
canva = Canvas(width=200, height=200)
get_logo_img = PhotoImage(file="logo.png")
canva.create_image(115,100,image=get_logo_img)
canva.grid(column=4, row=1, columnspan=2,  sticky="we")


# Messagebox
def message_box(message):
    messagebox.showerror(
        title="Oh no",
        message=f"{message}"
    )

# Website - label & entery, search-button
website_label = Label(text="Website:")
website_label.grid(column=3,  row=4)

website_entery = Entry(width=30)
website_entery.insert(END, "Website")
website_entery.grid(column=5,   row=4, sticky="w")

search_button = Button(text="Search", width=10, command=search_password)
search_button.grid(column=6,row=4,  sticky="we")



# Email - label & entery
email_label = Label(text="Email:")
email_label.grid(column=3,row=5 )

email_entery = Entry(width=46)
email_entery.insert(END, "email@test.com")
email_entery.grid(column=5, columnspan=2,  row=5, sticky="we" )



# Password - label, entery & button
password_label = Label(text="Password:")
password_label.grid(column=3,row=6 )

password_entery = Entry(width=30)
password_entery.grid(column=5, row=6,  sticky="w" )
# Genererar slumpmässigt lösenord vid start
generate_password()

password_button = Button(text="Generate", width=10, command=generate_password)
password_button.grid(column=6,row=6,  sticky="we")



# Add - button
add_button = Button(text="Add", width=39, command=save_password)
add_button.grid(column=5, columnspan=2, row=7,  sticky="we")

window.mainloop()
