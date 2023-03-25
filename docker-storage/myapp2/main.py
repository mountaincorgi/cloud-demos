import sqlite3

from flask import Flask, g, request  # g stores application context data


app = Flask(__name__)


# Create path to database (will be auto-created on connection if it 
# doesn't exist)
DATABASE = "/databases/myapp2.db"


def get_db():
    """If there's no database in context, establish a new connection."""

    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)

    # Return rows as tuples
    db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    """Close the database connection after every request."""

    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


# App routes
@app.route("/")
def hello_world():
    return "Hello world!"


@app.route("/all-flasks")
def all_flasks():
    """Show all types of flasks in the database."""
    db = get_db()
    cur = db.execute("select * from flasks")
    flasks = cur.fetchall()
    return "<br>".join([f"<p>{flask['name']}</p>" for flask in flasks])


@app.route("/add-flask", methods=["POST"])
def add_flask():
    """Add a new flask to our collection.
    
    Request body must be in the form {"name": <Flask Name>}
    """

    data = request.form
    new_flask_name = data.get("name")
    print(data)
    print(new_flask_name)

    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO flasks (name) VALUES (?)", [f"{new_flask_name}",])
    db.commit()
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
