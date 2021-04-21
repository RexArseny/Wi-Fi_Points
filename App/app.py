from classes import App, DatabaseConnect

web_app = App()
web_app.start(DatabaseConnect.database_name)
