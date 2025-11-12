import sqlite3

conn = sqlite3.connect("db.sqlite")
c = conn.cursor()

c.execute("SELECT * FROM waitlist")
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()