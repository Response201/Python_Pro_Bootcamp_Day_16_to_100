import os
import random
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, select
from dotenv import load_dotenv
load_dotenv()

# 📍 Postman api dokumentation:
# https://documenter.getpostman.com/view/17730586/2sBXihpsdJ

app = Flask(__name__)

# Skapa DB
class Base(DeclarativeBase):
    pass

# Koppla till Databas
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe Table
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")



# Hämta alla cafer eller alla cafer utifrån plats
@app.route("/cafes", methods=["GET"])
def get_cafes():
    loc = request.args.get("loc")
    query = select(Cafe)

    if loc:
        query = query.where(Cafe.location == loc)

    cafes = db.session.execute(query).scalars().all()

    cafe_list = []
    for cafe in cafes:
        cafe_list.append({
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
        })

    if cafe_list:
        return jsonify(cafe_list), 200

    return jsonify({"error": "No cafe found"}), 400




# Hämta ett slumpmässigt cafe
@app.route("/cafes/random", methods=["GET"] )
def random_cafe():
    cafe_list = db.session.execute(select(Cafe)).scalars().all()
    cafe = random.choice(cafe_list)
    return f"<h3> Random cafe is: {cafe.name} </h3>"




# Lägg till nytt cafe
@app.route("/cafes",  methods=["POST"])
def add():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    find_cafe = db.session.execute(select(Cafe).where(Cafe.name == data["name"])).first()

    if find_cafe:
        return jsonify({"error": "All ready exists"}), 400

    else:

        new_cafe = Cafe(
            name=data["name"],
            map_url=data["map_url"],
            img_url=data["img_url"],
            location=data["location"],
            seats=data["seats"],
            has_toilet=data["has_toilet"],
            has_wifi=data["has_wifi"],
            has_sockets=data["has_sockets"],
            can_take_calls=data["can_take_calls"],
            coffee_price=data["coffee_price"]
        )


        db.session.add(new_cafe)
        db.session.commit()
        return jsonify({
            "message": f"Cafe '{new_cafe.name}' added successfully!",
            "id": new_cafe.id
        }), 200



# Uppdatera kaffe-pris för ett cafe
@app.route("/cafes/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):

    cafe = db.session.execute(select(Cafe).where(Cafe.id == cafe_id)).scalar()
    data = request.get_json()
    new_price = data["coffee_price"]

    if cafe and new_price:

        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify({"message":f"Cafe: {cafe.name}'s coffee price updated to {new_price}"}), 200


    return jsonify({"error": "No cafe found"}), 400


# Radera ett cafe
@app.route("/cafes/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    key = request.headers.get("api-key")
    secret_key = os.getenv("SECRET_KEY")

    if not key or key != secret_key:
        return jsonify({"error": "Unauthorized"}), 401

    cafe = db.session.execute(select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify({"message": f"Cafe: {cafe.name} deleted"}), 200

    return jsonify({"error": "No cafe found"}), 400





if __name__ == '__main__':
    app.run(debug=True)
