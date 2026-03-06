

class GuessPage:
    def __init__(self):
        self.page_number = None
        self.random_number= None
        self.text = ""
        self.color ="black"
        self.image =""

    # Uppdaterar sidans innehåll(text, färg och bild) efter användarens gissning
    def update_page_content(self):

            if self.random_number == self.page_number:
                self.text = "You found me!"
                self.image="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
                self.color ="green"

            elif self.random_number > self.page_number:
                self.text = "Too low, try again"
                self.image = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
                self.color ="red"


            elif self.random_number < self.page_number:
                self.text = "Too high, try agin"
                self.image ="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
                self.color = "purple"



