
from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_data(url):
    response =requests.get(url)
    response.raise_for_status()

    return response.json()



@app.route("/")
def home():
    return render_template("api_index.html")


@app.route("/<name>")
def get_age(name):

    person = get_data(f"https://api.agify.io?name={name}")
    gender = get_data(f"https://api.genderize.io?name={name}")
    return render_template("api_age.html", age=person["age"], name=person["name"], gender=gender["gender"] )



if __name__ == "__main__":
    app.run(debug=True)