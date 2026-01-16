from turtle import Turtle

class TextWriter:
    def __init__(self):
        super().__init__()
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.color("white")

    # Skriver ut text
    def write_text(self, text, position, font_size=16, font_style="normal",color="white"):
        self.turtle.goto(position)
        self.turtle.color(color)
        self.turtle.write(
            text,
            align="center",
            font=("OCR A Extended", font_size, font_style)
        )

    # Tar bort text
    def clear(self):
        self.turtle.clear()
