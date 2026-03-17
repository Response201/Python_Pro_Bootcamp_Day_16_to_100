from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,  SelectField, TimeField, validators
from wtforms.validators import DataRequired,InputRequired, URL, ValidationError
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b-inte-hemlig'
Bootstrap5(app)


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.

# Skapar en dropdown med emoji-betyg
def create_dropdown(emoji, label_name):
    return SelectField(label=label_name,choices=[("✘"), (emoji), ((emoji * 2)), ((emoji * 3)), ((emoji * 4)), ((emoji * 5))])


class CafeForm(FlaskForm):
    emoijis = ["✘", "☕"]
    cafe = StringField('Cafe name', validators=[DataRequired(),validators.Length(min=3, max=20, message="Name must be between 3 and 20 characters." ) ])
    location = StringField( 'Location',validators=[InputRequired(), URL(message="Must be a valid URL")])
    open = TimeField('Open',format='%H:%M', validators=[DataRequired(message="Please enter the opening time")])
    close = TimeField('Close',format='%H:%M', validators=[DataRequired(message="Please enter the closing time")])
    coffee= create_dropdown("☕", "Coffee")
    wifi = create_dropdown("💪", "Wifi")
    power = create_dropdown("🔌", "Power")
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


# Exercise:
    # Make the form write a new row into cafe-data.csv
    # with if form.validate_on_submit()

@app.route('/add', methods=["GET", "POST"])
def add_cafe():

    form = CafeForm()
    if form.validate_on_submit():

        # Kontrollera att stängningstid är efter öppningstid
        if form.close.data <= form.open.data:
            form.close.errors.append("Closing time must be after opening time")
            return render_template('add.html', form=form)

        row = [form.cafe.data,
               form.location.data,
               form.open.data.strftime("%I:%M %p"),
               form.close.data.strftime("%I:%M %p"),
               form.coffee.data,
               form.wifi.data,
               form.power.data]

        # Spara cafet i CSV-filen
        with open("cafe-data.csv", mode="a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)

        return redirect("/cafes")
    return render_template('add.html', form=form)



# Visar alla cafer
@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
