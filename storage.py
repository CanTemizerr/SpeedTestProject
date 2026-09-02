import os
import sqlite3
from datetime import datetime
import pandas as pd

class database:
    def __init__(self):
        self.conn = sqlite3.connect("speedtest.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS speed_results (
            download REAL,
            upload REAL,
            ping REAL,
            time TEXT
        )
        """)
        self.conn.commit()

    def save_database(self, sonuc):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("""
        INSERT INTO speed_results (download, upload, ping, time)
        VALUES (?, ?, ?, ?)
        """, (sonuc['Download'], sonuc['Upload'], sonuc['Ping'], sonuc['Time']))
        self.conn.commit()
    def delete_db(self):
        self.cursor.execute('''
        DELETE FROM speed_result;
        '''
        )
    def get_result(self):
        con = sqlite3.connect("speedtest.db")
        df = pd.read_sql_query(
            'SELECT *FROM speed_results',
            con
        )
        con.close()
        return df




               


