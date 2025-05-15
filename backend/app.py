from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/message")
def message():
    return jsonify({"msg": "Hello from the backend!"})

if __name__ == "__main__":
    app.run(debug=True)