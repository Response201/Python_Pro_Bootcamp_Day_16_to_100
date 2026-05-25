
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
load_dotenv()
from functions import get_color_palette, save_image, delete_image

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config["IMAGE_FOLDER"] = "image"


@app.route("/", methods=["GET", "POST"])
def home():
    image_url=""
    image_color_palette = []
    delete_image()
    error= ""

    if request.method == "POST":
        try:
            image = request.files["imageUpload"]
            image_url = save_image(image)
            image_color_palette = get_color_palette(image)

        except Exception:
            error = "Ogiltig bildfil"


    return render_template(
        'base.html',
        image_url=image_url,
        image_color_palette = image_color_palette,
        error=error
    )




if __name__ == '__main__':
    app.run(debug=True)