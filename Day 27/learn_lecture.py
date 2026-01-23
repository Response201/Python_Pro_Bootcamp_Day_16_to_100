"""

import tkinter as tk
from tkinter import messagebox

#  Skapa huvudfönstret
tk_tk = tk.Tk()
window = tk_tk
window.title("Tkinter")
window.geometry("400x300")

#  Funktioner
def onclick_get_text():
    text = entry.get()                 # Hämta text från input
    label.config(text=f"Hello {text}!")            # Uppdatera label


def visa_check():
    print("Checkbox:", check_var.get())  # True / False

# Widgets
label = tk.Label(window, text="Hello Tkinter!")
label.pack(pady=5)  # pady = vertikalt mellanrum

entry = tk.Entry(window)
entry.pack(pady=5)

button = tk.Button(window, text="Change greeting", command=onclick_get_text)
button.pack(pady=5)

#  Checkbox
check_var = tk.BooleanVar()
check = tk.Checkbutton(
    window,
    text="I <3 Python",
    variable=check_var,
    command=visa_check
)
check.pack(pady=5)

#  Grid-exempel
frame = tk.Frame(window)
frame.pack(pady=10)

tk.Label(frame, text="Name:").grid(row=0, column=0)
tk.Entry(frame).grid(row=0, column=1)

tk.Label(frame, text="Age:").grid(row=1, column=0)
tk.Entry(frame).grid(row=1, column=1)

#  Starta programmet
window.mainloop()

 """


# *args & **kwargs


# *args
def convert(*args):

    return sum(args)


print( convert(3,3,10)   )


# **kwargs - keyword arguments,  använd .get() för att undvika fel (KeyError) om ett värde saknas

def describe_cat(**cat_info):
    print(f"The cat's name is {cat_info['name']} and it is a {cat_info.get('breed')}.")

describe_cat(name="Molly", breed="Siberian")


def test(*args):
    print(args)


test(1, 2, 3, 5)