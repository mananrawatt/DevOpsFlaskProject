from login import is_login_pod_running
from flask import jsonify


# Checks whether login is running or not,If not, you're not allowed to login into the application
def health():
    try:
        pod_status = is_login_pod_running()
        if pod_status:
            return jsonify({"status": "Pod is running"}), 200
        else:
            return jsonify({"status": "Pod is not running"}), 503
    except Exception as e:
        return jsonify({"error": f"Error checking pod health: {str(e)}"}), 500
