from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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
    website = website_entery.get()
    email = email_entery.get()
    password = password_entery.get()

    # Kontrollerar så att inga fält är tomma
    if not website or not email or not password:
        messagebox.showerror(
            title="Oh no",
            message="Please don't leave any fields empty!"
        )
        return

    # Frågar användaren om uppgifterna ska sparas
    save = messagebox.askokcancel(title=website, message=f"These are the details entered:\n\n Website: {website}\n Email: {email}\n Password: {password}\n\n It is ok to save?")

    if save:
                with open("data.csv", mode="a") as file:
                    file.write(f"{website}, {email}, {password}\n")

                website_entery.delete(0, END)
                website_entery.insert(END, "Website 123")
                password_entery.delete(0,END)
                generate_password()



# ---------------------------- UI SETUP ------------------------------- #

# Logo-bild
canva = Canvas(width=200, height=200)
get_logo_img = PhotoImage(file="logo.png")
canva.create_image(115,100,image=get_logo_img)
canva.grid(column=4, row=1, columnspan=2,  sticky="we")


# Website - label & entery
website_label = Label(text="Website:")
website_label.grid(column=3,  row=4)

website_entery = Entry(width=46)
website_entery.insert(END, "Website")
website_entery.grid(column=5, columnspan=2,  row=4, sticky="we")



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
