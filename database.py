import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",        # default laragon
            database="tbm_kunjungan"
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.cursor

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
