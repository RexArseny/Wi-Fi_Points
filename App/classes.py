import requests
import sqlite3
from flask import Flask, render_template

url = 'https://apidata.mos.ru/v1/datasets/2756/rows?api_key=f9c0be7f31f63dd7556f10b62cafc58a'
database_name = 'database.db'
sql_name = 'information.sql'
html_name = 'index.html'


class Database:

    def request(self, url):
        response = requests.get(url)
        data = response.json()
        return data

    def connect(self, database_name, sql_name, data):
        connection = sqlite3.connect(database_name)

        with open(sql_name) as f:
            connection.executescript(f.read())

        cur = connection.cursor()

        for inf in data:
            cur.execute("INSERT INTO points (place, amount, name, func) VALUES (?, ?, ?, ?)", (
            inf["Cells"]["Location"], inf["Cells"]["NumberOfAccessPoints"], inf["Cells"]["WiFiName"],
            inf["Cells"]["FunctionFlag"]))

        connection.commit()
        connection.close()


class App:

    def start(self):
        app = Flask(__name__)

        @app.route('/')
        def index():
            conn = sqlite3.connect(database_name)
            conn.row_factory = sqlite3.Row
            points = conn.execute('SELECT * FROM points').fetchall()
            conn.close()
            return render_template(html_name, points=points)

        app.run()
