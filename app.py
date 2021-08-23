import sqlite3
from flask import Flask, render_template
from threading import Thread
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


if __name__ == "__main__":
    thread1 = Thread(target=app.run)
    thread2 = Thread(target=Update().update_24)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
