import sqlite3


def create_table(cursor):
    try:
        cursor.execute(""" CREATE TABLE IF NOT EXISTS currency (
            currency_id INTEGER PRIMARY KEY NOT NULL,
            currency_gold INTEGER NOT NULL,
            currency_silver INTEGER NOT NULL,
            currency_copper INTEGER NOT NULL,
            characters_id INTEGER NOT NULL)
        """)

    except sqlite3.OperationalError as e:
        print('sqlite error: ', e.args[0])
