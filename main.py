from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask("app")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db = SQLALchemy(app)

class Fitness(db.Model):
  id = db.Column(db.Integer, primary_kay=True)
  username = db.Column(db.String(120), Unique=True, nullable=False)
  minutes_active = db.Column(db.Integer(3), Unique=True, nullable=False)
  favorite_exercises= db.Column(db.String(500), Unique=False, nullable=False)

db.create_all()
db.session.commit()

new_user1 = Fitness(id=1,username="Diana",email="DianaMishleau@gmail.com",minutes_active=150,favorite_exercises="Yoga,Running,Cycling" )
db.session.add(new_user1)
 
db.session.commit()

search = Fitness.query.filter_by(minutes_active=60).first() 
print(search)

delete_diana = Fitness.query.filter_by(username="Diana").first()
if delete_diana:
    db.session.delete(delete_diana)
    db.session.commit()

def fitness_data():
  username = request.form.get("username")
  email = request.form.get("email")
  minutes_active = request.form.get("minutes_active")
  favorite_exercises = request.form.get("favorite_exercises")
  fitness_form = Fitness.query.filter_by(username=username).first()
  if not fitness_form:
    new_user = Fitness(username=username, email=email, minutes_active=minutes_active, fitness_form=fitness_form)
  db.session.add(new_user)
  db.session.commit()

def __repr__(self):
  return "<This week " + self.username + "worked out" + self.minutes_active + ">"

@app.route("/")
def fitness_info():
  return render_template("fitness_app.html")

app.run(host="0.0.0.0", port=8080)