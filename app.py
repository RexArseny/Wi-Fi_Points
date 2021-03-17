import sqlite3
from flask import Flask, render_template


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)


@app.route('/')
def index():
    conn = get_db_connection()
    points = conn.execute('SELECT * FROM points').fetchall()
    conn.close()
    print('index.html')
    return render_template('index.html', points=points)


app.run()
