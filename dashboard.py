from flask import render_template, session, flash, redirect, url_for
from kubernetes import client, config

def is_dashboard_pod_running():
    """
    Checks if the dashboard pod is running using the Kubernetes API.
    Returns True if the pod is running, False if it is down.
    """
    try:
        config.load_kube_config()  # Load Kubernetes configuration
        v1 = client.CoreV1Api()
        pods = v1.list_namespaced_pod(namespace="miniflask")  # Replace with the correct namespace

        for pod in pods.items:
            if "dashboard" in pod.metadata.name:  # Replace 'dashboard' with a unique identifier for the dashboard pod
                pod_status = pod.status.phase
                if pod_status == "Running":
                    return True  # Pod is running
                else:
                    print(f"Pod {pod.metadata.name} is not running. Status: {pod_status}")
                    return False  # Pod is not running

        return False  # No pod found with 'dashboard' in the name

    except Exception as e:
        print(f"Error checking dashboard pod status: {e}")
        return False

def dashboard():
    """
    Handles the dashboard route.
    Ensures the user is logged in before granting access.
    Displays the pod status message.
    """
    if not session.get("logged_in"):
        flash("You must log in to access the dashboard.", "warning")
        return redirect(url_for("login"))

    # Check if the dashboard pod is running
    pod_status = is_dashboard_pod_running()

    if pod_status:
        # If the pod is running, show the normal dashboard message
        return render_template("dashboard.html", message="Dashboard is running!")
    else:
        # If the pod is not running, show a service unavailable message
        flash("Dashboard functionality is temporarily unavailable. Please try again later.", "danger")
        return render_template("dashboard.html", message="Dashboard functionality is down, but you have successfully logged into the application.")
