import sqlite3

class DATABASE:
    def __init__(self) -> None:
        self.data_nube = {}
        self.name_database = "kailand_database.db"

    def build(self):
        with sqlite3.connect(self.name_database) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS launcher(
                                configVersion TEXT,
                                launcherVersion TEXT,
                                launcherUrl TEXT,
                                updateDescription TEXT,
                                reglas TEXT,
                                horario TEXT,
                                mods TEXT,
                                complementos TEXT
                            )
            ''')