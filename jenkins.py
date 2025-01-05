import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


def login_to_jenkins(url, username, password):
    """
    Logs into Jenkins and verifies login success.
    Returns:
        (str, bool): message and success status
    """
    try:
        response = requests.get(url, auth=(username, password))
        if response.status_code == 200:
            return "Login successful", True
        else:
            return "Invalid credentials, please try again.", False
    except Exception as e:
        return f"Error: {e}", False


def get_jenkins_pipelines(url, username, password):
    """
    Fetches the list of Jenkins pipelines with their statuses after login.
    Returns:
        list: List of pipelines with details (name, status, URL)
    """
    try:
        # Send a request to Jenkins API to fetch job details
        response = requests.get(f"{url}/api/json", auth=(username, password))

        if response.status_code == 200:
            data = response.json()
            pipelines = []

            # Extracting the list of jobs (pipelines) and their details
            for job in data['jobs']:
                pipeline_info = {
                    'name': job['name'],
                    'url': job['url'],
                    'status': job['color']  # Jenkins job color (status)
                }
                pipelines.append(pipeline_info)

            return pipelines
        else:
            return {"error": "Unable to fetch Jenkins pipelines"}
    except Exception as e:
        return {"error": f"Error fetching pipelines: {e}"}







# # jenkins.py
#
# import requests
#
# def get_jenkins_status():
#     """
#     Fetches the Jenkins server status.
#     Returns:
#         str: Status of Jenkins.
#     """
#     try:
#         response = requests.get("http://localhost:8080")
#         if response.status_code == 200:
#             return "Jenkins is running."
#         else:
#             return "Jenkins is not responding."
#     except Exception as e:
#         return f"Error connecting to Jenkins: {e}"
#
# def get_pipeline_details():
#     """
#     Fetches details of Jenkins pipelines.
#     Returns:
#         dict: Details of the pipelines with their statuses.
#     """
#     # Example hardcoded pipelines. Replace with actual API calls.
#     return {
#         "Pipeline 1": "Success",
#         "Pipeline 2": "Failed",
#         "Pipeline 3": "Running"
#     }
#
# def login_to_jenkins(jenkins_url, username, password):
#     """
#     Logs into the Jenkins server using the provided credentials.
#     Args:
#         jenkins_url (str): Jenkins server URL.
#         username (str): Username for Jenkins login.
#         password (str): Password for Jenkins login.
#     Returns:
#         tuple: Success or error message and authentication status (True/False).
#     """
#     try:
#         # Sending request with credentials for authentication
#         response = requests.get(jenkins_url, auth=(username, password))
#         if response.status_code == 200:
#             return "You are successfully logged into Jenkins.", True
#         elif response.status_code == 401:
#             return "Login failed: Invalid credentials.", False
#         else:
#             return f"Login failed: Unexpected error with status code {response.status_code}.", False
#     except Exception as e:
#         return f"Error connecting to Jenkins: {e}", False
#
#
# def get_jenkins_pipelines():
#     """
#     Fetches the list of Jenkins pipelines with their statuses.
#     Returns:
#         list: List of dictionaries containing pipeline name, status, and URL.
#     """
#     jenkins_url = "http://localhost:8080/api/json"
#     try:
#         # Sending a request to the Jenkins API to get pipeline information
#         response = requests.get(jenkins_url)
#         if response.status_code == 200:
#             data = response.json()
#             pipelines = []
#
#             # Example: Extracting pipelines from the response (this is based on Jenkins API structure)
#             for job in data['jobs']:
#                 pipeline_info = {
#                     'name': job['name'],
#                     'url': job['url'],
#                     'status': job.get('color', 'Unknown')  # Jenkins job color status (green, red, blue, etc.)
#                 }
#                 pipelines.append(pipeline_info)
#
#             return pipelines
#         else:
#             return {"error": "Unable to fetch Jenkins pipelines"}
#     except Exception as e:
#         return {"error": f"Error fetching pipelines: {e}"}