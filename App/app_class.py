import sqlite3
from functools import lru_cache
from flask import Flask, render_template, request
from base_class import Base
from request_class import DatabaseRequest
from connect_class import DatabaseConnect


class App(Base):
    html_name = 'index.html'

    @lru_cache()
    def start(self, database_name):
        app = Flask(__name__)

        # @app.route('/', methods=['GET', 'POST'])
        @app.route('/')
        def index():
            # if request.method == 'POST':
            #    db_request = DatabaseRequest()
            #    db_request.request()
            #    db_connect = DatabaseConnect()
            #    db_connect.connect(DatabaseRequest.json_name)
            #    conn = sqlite3.connect(database_name)
            #    conn.row_factory = sqlite3.Row
            #    points = conn.execute('SELECT * FROM points').fetchall()
            #    conn.close()
            #    return render_template(self.html_name, points=points)
            # else:
            #    conn = sqlite3.connect(database_name)
            #    conn.row_factory = sqlite3.Row
            #    points = conn.execute('SELECT * FROM points').fetchall()
            #    conn.close()
            #    return render_template(self.html_name, points=points)

            conn = sqlite3.connect(database_name)
            conn.row_factory = sqlite3.Row
            points = conn.execute('SELECT * FROM points').fetchall()
            conn.close()
            return render_template(self.html_name, points=points)

        app.run()
