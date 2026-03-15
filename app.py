from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Believe in yourself",
    "Success comes from consistency",
    "Never stop learning",
    "Dream big and work hard"
]

@app.route("/")
def home():
    return "Welcome Kumar! Use /quote to get a quote."

@app.route("/quote")
def quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run()