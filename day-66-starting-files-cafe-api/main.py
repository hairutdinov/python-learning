from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from random import choice
from werkzeug.exceptions import NotFound


API_KEY = 'TopSecretAPIKey'

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__._columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    

@app.route('/random')
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = choice(all_cafes)
    return jsonify(
        cafe=random_cafe.to_dict()
    )


@app.route('/all')
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify(
        cafes=[cafe.to_dict() for cafe in all_cafes]
    )


@app.route('/search')
def get_cafe_at_location():
    query_location = request.args.get('loc')
    result = db.session.execute(
        db.select(Cafe).order_by(Cafe.name).where(Cafe.location == query_location)
    )
    all_cafes = result.scalars().all()
    if not all_cafes:
        return jsonify(
            error={
                'Not Found': 'Sorry, we don\'t have a cafe at that location.'
            }
        )
    return jsonify(
        cafes=[cafe.to_dict() for cafe in all_cafes]
    )


@app.route('/add', methods=['POST'])
def create_cafe():
    print(request.form.get('loc'))
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    new_price = request.form.get('new_price')
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(success="Successfully updated the price.")


@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def report_cafe_closed(cafe_id):
    api_key = request.headers.get('api-key')
    if api_key != API_KEY:
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key."), 403
    try:
        cafe = db.get_or_404(Cafe, cafe_id)
    except NotFound:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200


if __name__ == '__main__':
    app.run(debug=True, port=8000)
