from texts import texts
import tkinter as tk
import time
import random

start_time = None

def start_timer(event):
    global start_time
    if start_time is None:
        start_time = time.time()

def calculate_accuracy(original, typed):
    correct = 0
    length = len(original)

    for i in range(min(len(typed), length)):
        if typed[i].lower() == original[i].lower():
            correct += 1

    return (correct / length) * 100 if length > 0 else 0

def calculate_results():
    global start_time
    if start_time is None:
        return

    typed = text.get("1.0", tk.END).strip()
    elapsed = time.time() - start_time

    wpm = int(len(typed.split()) / (elapsed / 60)) if elapsed > 0 else 0

    original = sample.cget("text").strip()
    accuracy = calculate_accuracy(original, typed)

    result.config(
        text=f"Ord per minut: {wpm} | Korrekthet: {accuracy:.2f}%", pady=5
    )

    check_button.pack_forget()

def reset_test():
    global start_time
    start_time = None

    text.delete("1.0", tk.END)
    sample.config(text=random.choice(texts))
    result.config(text="")
    check_button.pack()


root = tk.Tk()
root.title("Skrivtest")

sample = tk.Label(root, text=random.choice(texts), wraplength=300)
sample.pack(pady=10)

text = tk.Text(root, height=5, width=40)
text.pack()
text.bind("<Key>", start_timer)

check_button = tk.Button(root, text="Kontrollera", command=calculate_results)
check_button.pack()

reset_button = tk.Button(root, text="Starta om", command=reset_test)
reset_button.pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()