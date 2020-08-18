"""
This file is initially ran through database.py function database_setup(). The main purpose of this file is to
create the table for currencies in the game.

Current Currencies:
    - Gold
    - Silver
    - Copper
"""

import sqlite3


def create_table(cursor):
    """
    This function is used to initially create the table. It should not be called again unless the database is being
    reset. Should only be called in database.py database_setup().
    :param cursor: sqlite3 cursor object
    """
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
