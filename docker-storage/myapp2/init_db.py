import sqlite3

from main import DATABASE


connection = sqlite3.connect(DATABASE)


with open("./schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO flasks (name) VALUES (?)", ["Volumetric",])
cur.execute("INSERT INTO flasks (name) VALUES (?)", ["Conical",])
# Round-bottom flask

connection.commit()
connection.close()
