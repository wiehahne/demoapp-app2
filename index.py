from flask import Flask
from flask import send_file
app = Flask(__name__)
@app.route('/winter')
def summer():
    return "Winter App"
@app.route('/winter/amsterdam')
def amsterdam():
    filename = 'amsterdam-480x300.jpg'
    return send_file(filename, mimetype='image/gif')
@app.route('/winter/chicago')
def chicago():
    filename = 'chicago-480x300.jpg'
    return send_file(filename, mimetype='image/gif')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)