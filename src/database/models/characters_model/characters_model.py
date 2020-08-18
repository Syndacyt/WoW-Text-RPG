"""
This file contains many of the functions used to load and save data to the database.

Functions:
    - create_table()    - Creates the initial table to hold character data
"""

import sqlite3


def create_table(cursor):
    """
    This function is used to initially create the table. It should not be called again unless the database is being
    reset. Should only be called in database.py database_setup().
    :param cursor: sqlite3 cursor object
    """
    try:
        cursor.execute(""" CREATE TABLE IF NOT EXISTS characters (
        characters_id INTEGER PRIMARY KEY NOT NULL,
        characters_name TEXT NOT NULL,
        characters_level INTEGER NOT NULL,
        characters_experience INTEGER NOT NULL,
        classes_id INTEGER NOT NULL,
        races_id INTEGER NOT NULL,
        specializations_id INTEGER NOT NULL)
        """)
    except sqlite3.OperationalError as e:
        print('sqlite error: ', e.args[0])
