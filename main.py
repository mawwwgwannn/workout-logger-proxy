from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GOOGLE_SCRIPT_WEBHOOK = "https://script.google.com/macros/s/AKfycbxcYmiMIcK2TXfsD4_wKQFRITl8troA8Xg_LIjayptjn-JLKi8PKb1-lxsq0O1ySJcouQ/exec"

@app.route('/')
def index():
    return "Workout Logger Proxy is Live"

@app.route('/log-workout', methods=['POST'])
def log_workout():
    try:
        data = request.get_json()
        res = requests.post(GOOGLE_SCRIPT_WEBHOOK, json=data)
        return jsonify({"forwarded": True, "response": res.text}), res.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
