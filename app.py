from flask import Flask, render_template, request, redirect, url_for, session, flash
from login import login_user  # Importing the login functionality from login.py

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "supersecretkey"  # Replace with a secure secret key for session management


# Route for the login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Call the login function from login.py
        if login_user(username, password):
            session["logged_in"] = True
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))

    return render_template("login.html")  # here the login.html is taken from templates directory


# Route for the dashboard page
@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        flash("You must log in to access the dashboard.", "warning")
        return redirect(url_for("login"))

    return render_template("dashboard.html", message="Welcome to the Dashboard!")


# Route for logging out
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
