from text import TextWriter

class ScoreBoard(TextWriter):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_score()

    # Skriver ut poäng
    def write_score(self):
        self.clear()
        self.write_text(f"Score: {self.score}", 0, 260, 16, "normal")

    # Ökar och skriver ut poäng
    def increment_score(self):
        self.score += 1
        self.write_score()
