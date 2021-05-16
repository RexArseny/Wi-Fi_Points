import json
import requests
from functools import lru_cache
from base_class import Base


class DatabaseRequest(Base):
    key = open('key.txt', 'r')
    key = key.read()
    url = 'https://apidata.mos.ru/v1/datasets/2756/rows?api_key=' + key

    @lru_cache()
    def request(self):
        response = requests.get(self.url)
        data = open(self.json_name, 'w')
        json.dump(response.json(), data, ensure_ascii=False)
        data.close()
