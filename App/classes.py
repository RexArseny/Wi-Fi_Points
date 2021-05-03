import requests
import sqlite3
import json
import schedule
import time
from functools import lru_cache
from flask import Flask, render_template, request


class Update:
    @lru_cache()
    def update(self):
        db_request = DatabaseRequest()
        db_request.request()

        db_connect = DatabaseConnect()
        db_connect.connect(DatabaseRequest.json_name)

    def update_24(self):
        schedule.every(24).hours.do(self.update())

        while True:
            schedule.run_pending()
            time.sleep(1)


class DatabaseRequest:
    url = 'https://apidata.mos.ru/v1/datasets/2756/rows?api_key='
    json_name = 'data.json'

    @lru_cache()
    def request(self):
        response = requests.get(self.url)
        data = open(self.json_name, 'w')
        json.dump(response.json(), data, ensure_ascii=False)
        data.close()


class DatabaseConnect:
    database_name = 'database.db'
    sql_name = 'information.sql'

    @lru_cache()
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

    @lru_cache()
    def start(self, database_name):
        app = Flask(__name__)

        @app.route('/', methods=['GET', 'POST'])
        def index():
            if request.method == 'POST':
                db_request = DatabaseRequest()
                db_request.request()

                db_connect = DatabaseConnect()
                db_connect.connect(DatabaseRequest.json_name)

                conn = sqlite3.connect(database_name)
                conn.row_factory = sqlite3.Row
                points = conn.execute('SELECT * FROM points').fetchall()
                conn.close()
                return render_template(self.html_name, points=points)

            else:
                conn = sqlite3.connect(database_name)
                conn.row_factory = sqlite3.Row
                points = conn.execute('SELECT * FROM points').fetchall()
                conn.close()
                return render_template(self.html_name, points=points)

        app.run()
