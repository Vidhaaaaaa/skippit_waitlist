from flask import Flask, render_template, request
import sqlite3
import os

from createdb import DB_PATH, init_db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/join", methods=["POST"])
def join():
    email = request.form.get('email')

    if not email:
        return render_template('index.html', success="Please enter a valid email.")

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    try:
        c.execute("INSERT INTO waitlist (email) VALUES (?)", (email,))
        conn.commit()
        msg = "You’re in the waitlist 🕊️"
    except sqlite3.IntegrityError:
        msg = "You’re already on the list!"
    finally:
        conn.close()

    return render_template('index.html', success=msg)

@app.route("/ping")
def ping():
    return "im alive!"

if __name__ == '__main__':
    init_db()  # ensures the table exists
    app.run(debug=True)