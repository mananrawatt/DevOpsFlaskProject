from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from login import login_user  # Importing the login functionality from login.py
from login import is_login_pod_running
from templates.Pages.pages import register_routes
from dashboard import dashboard
from health import health

# Initialize Flask app
app = Flask(__name__)
# app = Flask(__name__, template_folder=['templates', 'Pages'])
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
# @app.route("/dashboard")
# def dashboard():
#     if not session.get("logged_in"):
#         flash("You must log in to access the dashboard.", "warning")
#         return redirect(url_for("login"))
#
#     return render_template("dashboard.html", message="Welcome to the Dashboard!")

# Route for the dashboard page
app.add_url_rule('/dashboard', 'dashboard', dashboard)


# Route to check pod health
# @app.route("/health")
# def health():
#     try:
#         pod_status = is_login_pod_running()
#         if pod_status:
#             return jsonify({"status": "Pod is running"}), 200
#         else:
#             return jsonify({"status": "Pod is not running"}), 503
#     except Exception as e:
#         return jsonify({"error": f"Error checking pod health: {str(e)}"}), 500

app.add_url_rule('/heath', 'heath', health)


# Route for logging out
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


# Register routes from pages.py
register_routes(app)

# Run the app
if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)