import sqlite3

from src import constants


def create_table(cursor):
    """
    This function is used to initially create the table. It should not be called again unless the database is being
    reset. Should only be called in database.py database_setup().

    :param cursor: sqlite3 cursor object
    """

    try:
        cursor.execute(""" CREATE TABLE IF NOT EXISTS classes (
            classes_id INTEGER PRIMARY KEY,
            classes_name TEXT NOT NULL,
            races_id INTEGER NOT NULL)
        """)

    except sqlite3.OperationalError as e:
        print('sqlite error: ', e.args[0])


def insert_classes(cursor):
    # Query to insert data into classes table
    query = "INSERT INTO classes(classes_name, races_id) VALUES (?, ?)"

    # Loop through each race(key) for each (value) to insert into database
    for key in constants.CLASS_RACE_IDS:
        for value in constants.CLASS_RACE_IDS[key]:
            cursor.execute(query, (key, value))




