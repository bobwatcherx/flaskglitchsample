from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(message="hello from glitch")

if __name__ == "__main__":
	app.run()