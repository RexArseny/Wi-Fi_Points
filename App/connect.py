from classes import DatabaseRequest, DatabaseConnect

db_connect = DatabaseConnect()
db_connect.connect(DatabaseRequest.json_name)
