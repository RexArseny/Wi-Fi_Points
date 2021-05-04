import time
import schedule
from functools import lru_cache
from request_class import DatabaseRequest
from connect_class import DatabaseConnect


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
