import json
import sqlite3
from functools import lru_cache
from base_class import Base


class DatabaseConnect(Base):
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
