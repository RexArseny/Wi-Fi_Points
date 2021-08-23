import time
import json
import sqlite3
import requests
import schedule


class DatabaseRequest:
    json_name = 'data.json'
    key = open('key.txt', 'r')
    url = 'https://apidata.mos.ru/v1/datasets/2756/rows?api_key=' + key.read()

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

        for dat in json_data:
            cur.execute("INSERT INTO points (place, amount, name, func) VALUES (?, ?, ?, ?)", (
                dat["Cells"]["Location"], dat["Cells"]["NumberOfAccessPoints"], dat["Cells"]["WiFiName"],
                dat["Cells"]["FunctionFlag"]))

        connection.commit()
        connection.close()


class Update:
    def __update(self):
        db_request = DatabaseRequest()
        db_request.request()

        db_connect = DatabaseConnect()
        db_connect.connect(DatabaseRequest.json_name)

    def update_24(self):
        schedule.every(24).hours.do(self.__update)

        while True:
            schedule.run_pending()
            time.sleep(1)
