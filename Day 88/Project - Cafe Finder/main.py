import os
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from database import database
from functions import filter
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap5(app)

db, Cafe = database(app)


@app.route("/", methods=["GET"])
@app.route("/<int:cafe_id>", methods=["GET"])
def home(cafe_id=None):

    cafes, form = filter(request.args, Cafe)

    if form.reset.data:
        return redirect(url_for("home", cafe_id=cafe_id))


    selected_cafe = Cafe.query.get(cafe_id)

    if selected_cafe:
        selected_cafe_map = f"https://www.google.com/maps?q={selected_cafe.name}+{selected_cafe.location}&output=embed"
    else:
        selected_cafe_map = ""


    return render_template(
        'cafes.html',
        cafes=cafes,
        selected_cafe=selected_cafe,
        selected_cafe_map=selected_cafe_map,
        form=form
    )



if __name__ == '__main__':
    app.run(debug=True)