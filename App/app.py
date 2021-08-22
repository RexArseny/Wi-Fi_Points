import sqlite3
from flask import Flask, render_template
from model import Update

html_name = 'index.html'
database_name = 'database.db'
app = Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect(database_name)
    conn.row_factory = sqlite3.Row
    points = conn.execute('SELECT * FROM points').fetchall()
    conn.close()
    return render_template(html_name, points=points)


app.run()

# Update().update_24()
