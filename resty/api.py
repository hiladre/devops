from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)


@app.route('/api/v1/trigger', methods=['POST'])
def trigger_job():
    data = request.get_json()
    if not data or 'id' not in data:
        return jsonify({"error": "Missing ID parameter"}), 400

    job_id = data['id']
    result = subprocess.run([
        "kubectl", "create", "job", f"rowy-job-{job_id}",
        "--from=cronjob/rowy-template",
        f"--env=JOB_ID={job_id}"
    ], capture_output=True)

    if result.returncode == 0:
        return jsonify({"message": "Job triggered successfully"}), 200
    else:
        return jsonify({"error": result.stderr.decode()}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
