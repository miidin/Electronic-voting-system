from flask import Flask, render_template, request, jsonify
from auth import send_otp, verify_otp
from database import init_db

app = Flask(__name__)

# Initialize database
init_db(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send-otp", methods=["POST"])
def send_otp_route():
    data = request.json
    return send_otp(data["phone"])

@app.route("/verify-otp", methods=["POST"])
def verify_otp_route():
    data = request.json
    return verify_otp(data["otp"])

if __name__ == "__main__":
    app.run(debug=True)
