from flask import Flask, render_template, request, redirect, url_for
from model import db, User
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="web")

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:4951249@localhost/caregiver"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def home():
    return redirect(url_for('list_users'))

@app.route("/users")
def list_users():
    users = User.query.all()
    return render_template("users_list.html", users=users)


@app.route("/users/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        email = request.form["email"]
        given_name = request.form["given_name"]
        surname = request.form["surname"]

        user = User(email=email, given_name=given_name, surname=surname)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("list_users"))

    return render_template("user_form.html", user=None, action="Create")


@app.route("/users/edit/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    user = User.query.get_or_404(id)

    if request.method == "POST":
        user.email = request.form["email"]
        user.given_name = request.form["given_name"]
        user.surname = request.form["surname"]
        db.session.commit()
        return redirect(url_for("list_users"))

    return render_template("user_form.html", user=user, action="Edit")


@app.route("/users/delete/<int:id>", methods=["POST"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("list_users"))

if __name__ == "__main__":
    app.run(debug=True)
