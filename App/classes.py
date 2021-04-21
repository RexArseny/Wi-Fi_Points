import requests
import sqlite3
import json
from flask import Flask, render_template


class DatabaseRequest:
    url = 'https://apidata.mos.ru/v1/datasets/2756/rows?api_key='
    json_name = 'data.json'

    def request(self):
        response = requests.get(self.url)
        data = open(self.json_name, 'w')
        json.dump(response.json(), data, ensure_ascii=False)
        data.close()


class DatabaseConnect:
    database_name = 'database.db'
    sql_name = 'information.sql'

    def connect(self, json_name):
        data = open(json_name, 'r')
        json_data = json.load(data)

        connection = sqlite3.connect(self.database_name)
        with open(self.sql_name) as db:
            connection.executescript(db.read())

        cur = connection.cursor()

        for datas in json_data:
            cur.execute("INSERT INTO points (place, amount, name, func) VALUES (?, ?, ?, ?)", (
                datas["Cells"]["Location"], datas["Cells"]["NumberOfAccessPoints"], datas["Cells"]["WiFiName"],
                datas["Cells"]["FunctionFlag"]))

        connection.commit()
        connection.close()


class App:
    html_name = 'index.html'

    def start(self, database_name):
        app = Flask(__name__)

        @app.route('/')
        def index():
            conn = sqlite3.connect(database_name)
            conn.row_factory = sqlite3.Row
            points = conn.execute('SELECT * FROM points').fetchall()
            conn.close()
            return render_template(self.html_name, points=points)

        app.run()
