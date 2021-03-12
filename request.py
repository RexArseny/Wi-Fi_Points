import requests
import sqlite3

url = 'https://apidata.mos.ru/v1/datasets/2756/rows?api_key=f9c0be7f31f63dd7556f10b62cafc58a'

response = requests.get(url)
infs = response.json()


connection = sqlite3.connect('database.db')

with open('information.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

for inf in infs:
    cur.execute("INSERT INTO points (place, amount, name, func) VALUES (?, ?, ?, ?)",
            (inf["Cells"]["Location"], inf["Cells"]["NumberOfAccessPoints"], inf["Cells"]["WiFiName"], inf["Cells"]["FunctionFlag"])
            )

connection.commit()
connection.close()
