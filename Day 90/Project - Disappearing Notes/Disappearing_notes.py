import tkinter as tk
import time


class Disappearing_notes:
    def __init__(self, root):
        self.root = root
        self.root.title("Skriv utan att sluta – annars försvinner allt")

        self.running = False
        self.limit = 5
        self.last = time.time()

        self.top = tk.Frame(root)
        self.top.pack(fill="x")

        self.label = tk.Label(
            self.top,
            text="",
            bg="white",
            fg="black",
            font=("Arial", 14)
        )
        self.label.pack(fill="x")

        self.btn = tk.Button(self.top, text="START", command=self.start)
        self.btn.pack(fill="x")

        self.text = None

        self.loop()


    def start(self):
        self.running = True
        self.last = time.time()
        self.btn.pack_forget()

        self.text = tk.Text(self.root, font=("Arial", 14))
        self.text.pack(expand=True, fill="both")
        self.text.bind("<KeyPress>", self.reset_timer)


    def game_over(self):
        self.running = False

        if self.text:
            self.text.delete("1.0", tk.END)
            self.text.pack_forget()

        self.btn.pack(fill="x")

        self.label.config(
            text="DU DOG 💀",
            bg="black",
            fg="white"
        )


    def reset_timer(self, event=None):
        if self.running:
            self.last = time.time()

    def loop(self):
        if self.running:

            remaining = self.limit - (time.time() - self.last)
            text = self.text.get("1.0", "end-1c")
            chars = len(text)

            if remaining <= 0:
                self.game_over()
            else:
                if remaining < 2:

                    bg = "red"
                else:
                    bg = "yellow"

                self.label.config(
                    text=f"{chars} tecken | {remaining:.1f}s",
                    bg=bg, fg="black",
                )

        self.root.after(100, self.loop)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")
    Disappearing_notes(root)
    root.mainloop()