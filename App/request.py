from classes import DatabaseRequest, DatabaseConnect
import schedule
import time


def update():
    db_request = DatabaseRequest()
    db_request.request()

    db_connect = DatabaseConnect()
    db_connect.connect(DatabaseRequest.json_name)


schedule.every(24).hours.do(update)

while True:
    schedule.run_pending()
    time.sleep(1)
