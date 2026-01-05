from flask import Flask, render_template, request, send_from_directory
import requests
import sqlite3
import os

from createdb import DB_PATH, init_db

GOOGLE_SHEET_WEBHOOK = "https://script.google.com/macros/s/AKfycbyd92Xb3gxKGpte39OwAYeQ6bjWNfwnRtDlUbVlFgmb8q3J1e4MVmsx_CI0u27Pe1PXmw/exec"

app = Flask(__name__,template_folder="frontend/templates", static_folder="frontend/static")

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/")
def fixing():
    return render_template("fixing.html")

# @app.route("/join", methods=["POST"])
# def join():
#     email = request.form.get('email')

#     if not email:
#         return render_template('index.html', success="Please enter a valid email.")

#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()

#     try:
#         c.execute("INSERT INTO waitlist (email) VALUES (?)", (email,))
#         conn.commit()
#         msg = "You’re in the waitlist 🕊️"
#     except sqlite3.IntegrityError:
#         msg = "You’re already on the list!"
#     finally:
#         conn.close()

#     return render_template('index.html', success=msg)

@app.route("/join", methods=["POST"])
def join():
    email = request.form.get("email")

    if not email:
        return render_template("index.html", success="Please enter a valid email.")

    try:
        response = requests.post(
            GOOGLE_SHEET_WEBHOOK,
            json={"email": email},
            timeout=5
        )

        if response.status_code != 200:
            raise Exception("Failed to save email")

        return render_template("index.html", success="You’re in the waitlist 🕊️")

    except Exception as e:
        print("Error:", e)
        return render_template(
            "index.html",
            success="Something went wrong. Please try again."
        )

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(
#         os.path.join(app.static_folder, 'img'),
#         'favicon.png'
#     )

@app.route("/ping") # ping for render - every 10 mins
def ping():
    return "pong"

if __name__ == '__main__':
    init_db()  # ensures the table exists
    debug = os.environ.get("FLASK_ENV") == "development"
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=debug)