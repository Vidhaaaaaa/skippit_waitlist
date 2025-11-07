from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/join")
def join():
    return "hehehehe not yet"

if __name__ == '__main__':
    app.run(debug=True)