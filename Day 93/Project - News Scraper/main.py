from flask import Flask, render_template
from news_scraper import get_articels

app = Flask(__name__)

@app.route("/")

def index():
    

    articles = get_articels()
    return render_template("index.html", articles=articles)



if __name__ == "__main__":
    app.run(debug=True)