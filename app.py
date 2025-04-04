from flask import Flask
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return "Hello, DevOps with AI! Database Connected."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
