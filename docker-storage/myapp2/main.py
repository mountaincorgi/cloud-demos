import sqlite3

from flask import Flask, g, request  # g stores application context data


app = Flask(__name__)


# Create path to database (will be auto-created on connection if it 
# doesn't exist)
# We will use a VOLUME to persist this database
# We will use a BIND MOUNT to persist the code base
DATABASE = "/databases/myapp2.db"


def get_db():
    """If there's no database in context, establish a new connection."""

    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
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


@app.route("/get-all-flasks")
def lab_equipment(lab_equipment_id):
    """Get different types of flasks."""

    if lab_equipment_id not in [1, 2, 3]:
        return f"No lab equipment matches provided ID: {lab_equipment_id}"
    else:
        pass


@app.route("/add-flask", methods=["POST"])
def add_flask():
    """Add a new flask to our collection."""

    req = request
    db = get_db()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
