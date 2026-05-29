import os

from dotenv import load_dotenv
from flask import Flask, render_template
from functions import get_data
load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():

    cat_fact_data = get_data(os.getenv("FACT_URL"))
    cat_fact = cat_fact_data.get("fact") if cat_fact_data else None

    cat_image_data = get_data(os.getenv("IMAGE_URL"))
    cat_image = None
    if cat_image_data and len(cat_image_data) > 0:
        cat_image = cat_image_data[0].get("url")


    return render_template("index.html", fact=cat_fact,
                           image_url=cat_image)


if __name__ == "__main__":
    app.run(debug=True)
