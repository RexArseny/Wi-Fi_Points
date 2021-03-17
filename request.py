import requests

url = 'https://apidata.mos.ru/v1/datasets/2756/rows?api_key=f9c0be7f31f63dd7556f10b62cafc58a'

response = requests.get(url)
infs = response.json()
