from flask import render_template, request, redirect, url_for, flash
from jenkins import login_to_jenkins, get_jenkins_pipelines


def register_routes(app):
    # Register all page routes

    # @app.route("/jenkins")
    # def jenkins():
    #     return render_template("Pages/jenkins.html", title="Page 1 - jenkins")

    # @app.route('/jenkins')
    # def jenkins():
    #     """
    #     Fetches Jenkins details and renders the Jenkins page.
    #     """
    #     jenkins_status = get_jenkins_status()
    #     pipeline_details = get_pipeline_details()
    #     return render_template(
    #         'Pages/jenkins.html',
    #         status=jenkins_status,
    #         pipelines=pipeline_details
    #     )

    # @app.route('/jenkins', methods=['GET', 'POST'])
    # def jenkins():
    #     """
    #     Fetches Jenkins details and renders the Jenkins page.
    #     Handles Jenkins login and displays pipeline details upon successful login.
    #     """
    #     # Initial Jenkins status
    #     jenkins_status = get_jenkins_status()
    #
    #     if request.method == 'POST':
    #         # Get the username and password from the form
    #         username = request.form.get('username')
    #         password = request.form.get('password')
    #
    #         # Attempt to log in to Jenkins
    #         login_message, login_success = login_to_jenkins("http://localhost:8080", username, password)
    #
    #         if login_success:
    #             # If login is successful, fetch pipeline details
    #             pipeline_details = get_jenkins_pipelines()  # Fetch pipeline data here
    #             return render_template(
    #                 'Pages/jenkins.html',
    #                 status=jenkins_status,
    #                 pipelines=pipeline_details,
    #                 login_message=login_message,
    #                 logged_in=True
    #             )
    #         else:
    #             # If login failed, show error message and ask for credentials again
    #             flash(login_message)
    #             return render_template(
    #                 'Pages/jenkins.html',
    #                 status=jenkins_status,
    #                 login_message=login_message,
    #                 logged_in=False
    #             )
    #
    #     # Default view when page loads
    #     return render_template(
    #         'Pages/jenkins.html',
    #         status=jenkins_status,
    #         logged_in=False
    #     )

    @app.route('/jenkins', methods=['GET', 'POST'])
    def jenkins():
        """
        Handles Jenkins login, fetches pipelines, and returns details as text.
        """
        if request.method == 'POST':
            # Get username and password from the form
            username = request.form.get('username')
            password = request.form.get('password')

            # Attempt to log in to Jenkins
            login_message, login_success = login_to_jenkins("http://localhost:8080", username, password)

            if login_success:
                # If login is successful, fetch pipeline details
                pipeline_details = get_jenkins_pipelines("http://localhost:8080", username, password)

                # Creating a formatted list of pipelines with clickable URLs
                pipelines_str = '<ul>'
                for pipe in pipeline_details:
                    pipelines_str += f'''
                        <li>
                            <strong>Pipeline:</strong> {pipe['name']}<br>
                            <strong>Status:</strong> {pipe['status']}<br>
                            <strong>URL:</strong> <a href="{pipe['url']}" target="_blank">{pipe['url']}</a><br><br>
                        </li>
                    '''
                pipelines_str += '</ul>'

                # Return the formatted login message and pipelines details
                return f'''
                    <h3>{login_message}</h3>
                    <h4>Pipelines:</h4>
                    {pipelines_str}
                '''
            else:
                # If login fails, display the error message
                flash(login_message)
                return f"<h3>Login failed: {login_message}</h3>"

        # Default view when page loads (GET request)
        return '''
            <h3>Please log in to view Jenkins Pipelines</h3>
            <form method="POST">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required><br><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required><br><br>
                <button type="submit">Log In</button>
            </form>
        '''

    @app.route("/kubernetes")
    def kubernetes():
        return render_template("Pages/kubernetes.html", title="Page 2 - kubernetes")

    @app.route("/docker")
    def docker():
        return render_template("Pages/docker.html", title="Page 3 - docker")

    @app.route("/minikube")
    def minikube():
        return render_template("Pages/minikube.html", title="Page 4 - minikube")











# from flask import render_template, session, redirect, url_for, flash
# def register_routes(app):
#     @app.route("/page1")
#     def page1():
#         if not session.get("logged_in"):
#             flash("You must log in to access this page.", "warning")
#             return redirect(url_for("login"))
#         return render_template("Pages/jenkins.html", title="Page 1")
#
#     @app.route("/page2")
#     def page2():
#         if not session.get("logged_in"):
#             flash("You must log in to access this page.", "warning")
#             return redirect(url_for("login"))
#         return render_pages("kubernetes.html", title="Page 2")
#
#     @app.route("/page3")
#     def page3():
#         if not session.get("logged_in"):
#             flash("You must log in to access this page.", "warning")
#             return redirect(url_for("login"))
#         return render_template("Pages/docker.html", title="Page 3")
#
#     @app.route("/page4")
#     def page4():
#         if not session.get("logged_in"):
#             flash("You must log in to access this page.", "warning")
#             return redirect(url_for("login"))
#         return render_template("Pages/minikube.html", title="Page 4")
