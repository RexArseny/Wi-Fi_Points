from classes import Database, url, database_name, sql_name

database = Database()

data = database.request(url)

connection = database.connect(database_name, sql_name, data)
