import sqlite3
from request import data

connection = sqlite3.connect('database.db')

with open('information.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

for inf in data:
    cur.execute("INSERT INTO points (place, amount, name, func) VALUES (?, ?, ?, ?)", (inf["Cells"]["Location"], inf["Cells"]["NumberOfAccessPoints"], inf["Cells"]["WiFiName"], inf["Cells"]["FunctionFlag"]))

connection.commit()
connection.close()
