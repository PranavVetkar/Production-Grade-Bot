import sqlite3
from datetime import datetime

class MarketDB:
    def __init__(self, db_name="crypto_trading.db"):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS trade_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    symbol TEXT,
                    price REAL,
                    signal TEXT,
                    balance REAL
                )
            ''')
            conn.commit()

    def log_event(self, symbol, price, signal, balance):
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO trade_log (timestamp, symbol, price, signal, balance) VALUES (?, ?, ?, ?, ?)', 
                            (ts, symbol, price, signal, balance))
            conn.commit()