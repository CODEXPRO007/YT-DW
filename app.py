from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from ytdl import extract
from auth import check_key

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/download")
def api():
    url = request.args.get("url")
    key = request.headers.get("X-API-KEY")

    plan = check_key(key)
    if not plan:
        return jsonify({"error": "Invalid API Key"}), 403

    data = extract(url)

    if plan == "premium":
        data["audio"] = None   # free users audio disabled

    return jsonify(data)

app.run(host="0.0.0.0", port=5000)