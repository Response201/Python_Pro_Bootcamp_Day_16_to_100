import tkinter as tk

# Skapa fönster
window = tk.Tk()
window.title("Mile to Kilometers Converter")
window.minsize(width=400, height=180)

# Konfigurera 12 kolumner/rows så att de tar lika mycket plats
for i in range(12):  # 0–11 = 12 kolumner
    window.grid_columnconfigure(i, weight=1)
    window.grid_rowconfigure(i, weight=1)



# Konverterar miles till km och uppdaterar result_label med värdet
def convert_miles_to_km():
    mile_text = input_mile.get()
    try:
        miles = float(mile_text)
        kilometers = 1.609 * miles
        result_label["text"] = f"{round(kilometers, 2)}"
    except ValueError:
        print("wrong type")

# Knapp
button = tk.Button(text="Convert", command=convert_miles_to_km)
button.grid(column=6, row=7, padx=10, pady=5)



# Inmatning för miles
input_mile = tk.Entry(width=7)
input_mile.grid(column=6, row=5)


# Labels
heading_label = tk.Label(text="Miles", font=("Arial", 12, "normal") )
heading_label.grid(column=7, row=5, )


is_equal_label = tk.Label(text="is equal to", font=("Arial", 12))
is_equal_label.grid(column=5, row=6)

result_label = tk.Label(text="0", font=("Arial", 12), justify="center")
result_label.grid(column=6, row=6,  )

km_label = tk.Label(text="Km", font=("Arial", 12))
km_label.grid(column=8, row=6)




window.mainloop()
