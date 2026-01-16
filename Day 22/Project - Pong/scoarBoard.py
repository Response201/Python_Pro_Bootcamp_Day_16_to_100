from text import TextWriter

class ScoreBoard(TextWriter):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.position = position
        self.update()



    # Tar bort och skriver ut poäng
    def update(self):
        self.clear()
        self.write_text(
            text=str(self.score),
            position=self.position,
            font_size=62,
            font_style="normal"
        )

    # Updaterar poäng
    def add_point(self):
        self.score += 1
        self.update()