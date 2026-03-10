import random
import datetime as dt
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    test = "Hello world"
    random_number = random.randint(1,5)
    year = dt.datetime.now().year

    return render_template("index.html", test=test, random_num=random_number, this_year=year)



if __name__ == "__main__":
    app.run(debug=True)