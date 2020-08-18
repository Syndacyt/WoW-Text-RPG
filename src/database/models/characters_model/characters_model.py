import sqlite3


def create_table(cursor):
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
