from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

user_credential = {
    "username": "mani",
    "password": "1234"
}

@auth_bp.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == user_credential["username"] and password == user_credential["password"]:

            session["user"] = username
            flash("Login successful", "success")
            return redirect(url_for("task.view_task"))

        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():

    session.pop("user", None)
    flash("Logout successful", "info")

    return redirect(url_for("auth.login"))