import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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
        # Create a new dictionary entry;
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # where the key is the name of the column
                                     # and the value is the value of the column// getattr returns the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary



@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random_cafe():
    one_cafes = db.session.query(Cafe).all()
    cafe = random.choice(one_cafes)
    return jsonify(cafe=cafe.to_dict())


@app.route("/all_cafes")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    all = []
    for cafe in cafes:
       all.append(cafe.to_dict())
    return jsonify(all)


@app.route("/search")
def search():
    specified_location = request.args.get("location")

    #.one() requires that there is only one result in the result set. it is an error if the database returns 0 or 2 or more results
    # resulted_cafe = db.session.query(Cafe).filter(Cafe.location == location).one()

    # .first() returns the first eliment of the selected elements
    resulted_cafe = db.session.query(Cafe).filter_by(location= specified_location).first()
    if resulted_cafe:
        return jsonify(cafe = resulted_cafe.to_dict())
    else:
        return jsonify(error={"Cafe not found" : "there are no cafes in the specified location"})


## HTTP POST - Create Record
@app.route("/addcafe", methods=["POST"])
def adding():
    cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = request.form.get("has_toilet"),
        has_wifi = request.form.get("has_wifi"),
        has_sockets = request.form.get("has_sockets"),
        can_take_calls = request.form.get("can_take_calls"),
        coffee_price = request.form.get("coffee_price")
        )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response= { "Success" : "a new cafe is added"})



## HTTP PUT/PATCH - Update Record
@app.route("/update/<id>", methods = ["PATCH"])
def update(id):
    cafe = db.session.query(Cafe).filter_by(id=id).one()
    if cafe:
        cafe.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(response={"success": "data updated"})
    else:
        return jsonify(resource={"id not found": "data notfound"})

## HTTP DELETE - Delete Record
@app.route("/delete", methods=["DELETE"])
def delete():
    to_delete_id = request.args.get("id")
    cafe = db.session.query(Cafe).filter_by(id=to_delete_id).one()
    if cafe :
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response= {"success": f"cafe with id {to_delete_id} deleted"} )
    else:
        return jsonify(response={"Failure": f"cafe with id {to_delete_id} not found"})
if __name__ == '__main__':
    app.run(debug=True)
