from flask import render_template

def register_routes(app):
    # Register all page routes

    @app.route("/page1")
    def page1():
        return render_template("Pages/page1.html", title="Page 1")

    @app.route("/page2")
    def page2():
        return render_template("Pages/page2.html", title="Page 2")

    @app.route("/page3")
    def page3():
        return render_template("Pages/page3.html", title="Page 3")

    @app.route("/page4")
    def page4():
        return render_template("Pages/page4.html", title="Page 4")











# from flask import render_template, session, redirect, url_for, flash
# def register_routes(app):
#     @app.route("/page1")
#     def page1():
#         if not session.get("logged_in"):
#             flash("You must log in to access this page.", "warning")
#             return redirect(url_for("login"))
#         return render_template("Pages/page1.html", title="Page 1")
#
#     @app.route("/page2")
#     def page2():
#         if not session.get("logged_in"):
#             flash("You must log in to access this page.", "warning")
#             return redirect(url_for("login"))
#         return render_pages("page2.html", title="Page 2")
#
#     @app.route("/page3")
#     def page3():
#         if not session.get("logged_in"):
#             flash("You must log in to access this page.", "warning")
#             return redirect(url_for("login"))
#         return render_template("Pages/page3.html", title="Page 3")
#
#     @app.route("/page4")
#     def page4():
#         if not session.get("logged_in"):
#             flash("You must log in to access this page.", "warning")
#             return redirect(url_for("login"))
#         return render_template("Pages/page4.html", title="Page 4")
