from flask import Flask
app = Flask(__name__)
@app.route("/winter")
def hello():
    return "Winter!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)