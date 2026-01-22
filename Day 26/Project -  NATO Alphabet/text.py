from turtle import Turtle

class TextWriter:
    def __init__(self):
        super().__init__()
        self.text_code =""

    # Skriver ut text
    def write_text(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(0, 0)

        self.turtle.write(
            # Gör listan till sträng
            f"{" ".join(self.text_code)}",
            align="center",
            font=("Courier", 8, "normal")
        )
    # Tar bort text
    def clear(self):
        self.turtle.clear()
