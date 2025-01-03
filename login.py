from kubernetes import client, config
from flask import flash


# Function to check the status of the login pod
def is_login_pod_running():
    try:
        # Load Kubernetes configuration
        config.load_kube_config()
        v1 = client.CoreV1Api()

        # Check the status of the login pod
        pods = v1.list_namespaced_pod(namespace="miniflask", label_selector="app=login")
        for pod in pods.items:
            if pod.status.phase == "Running":
                return True
        return False
    except Exception as e:
        print(f"Error checking login pod status: {e}")
        return False


# Function for login validation
def validate_login(username, password):
    # Simulated validation (replace with actual logic)
    if username == "admin" and password == "password123":
        return True
    elif username == "devops" and password == "devops":
        return True
    else:
        flash("Invalid username or password. Please try again.", "danger")
        return False


# Function to handle login logic
def login_user(username, password):
    if not is_login_pod_running():
        flash("Login service is currently unavailable. Please try again later.", "danger")
        return False

    if validate_login(username, password):
        return True
    else:
        return False
