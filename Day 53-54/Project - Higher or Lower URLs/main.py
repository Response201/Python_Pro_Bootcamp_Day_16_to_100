import random
from flask import Flask
from guess_page import GuessPage

#Flask
app = Flask(__name__)


page = GuessPage()
page.random_number = random.randint(1, 9)


# Dekorator för att skapa html-sida
def create_html(func):

    def wrapper(*args, **kwargs):
        text, image, color = func(*args, **kwargs)
        return (
            f"<div style='width: 100%; min-height:95vh;  display: flex; justify-content: center; align-items: center; flex-direction: column;'>"
            f"<div style='width: 100%; height: fit-content; display: flex; justify-content: center; align-items: center; flex-direction: column;'>"
            f"<h1 style='color:{color}'>{text}</h1>"
            f"<img style='width: 500px; height: 500px; object-fit: cover;' src='{image}'>"
            f"</div>"
            f"</div>"

)
    return wrapper

# Startsida
@app.route("/")
@create_html
def index_html():
    text = "Welcome! Guess a number between 1 and 9"
    color = "black"
    image = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
    return text, image, color

# Sida för varje gissat nummer
@app.route("/<int:check_number>", endpoint="page_number")
@create_html
def page_number(check_number):
    page.page_number = check_number
    page.update_page_content()
    return page.text, page.image, page.color

# 404
@app.errorhandler(404)
@create_html
def not_found(e):
    text = ""
    image = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzY0eGdiZjBzOWx3NnZrYzFweHVnY3V1dTd4bXY4MDJ1cWF1Y3Y5diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pyLTnfIzYPnw8LEWWU/giphy.gif"
    color = "black"
    return text, image, color

if __name__ == "__main__":
    app.run(debug=True)