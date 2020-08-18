import sqlite3
from src import constants


def create_table(cursor):
    try:
        cursor.execute(""" CREATE TABLE IF NOT EXISTS races (
            races_id INTEGER PRIMARY KEY NOT NULL,
            races_name TEXT NOT NULL,
            races_faction TEXT NOT NULL)
        """)

    except sqlite3.OperationalError as e:
        print('sqlite error: ', e.args[0])


def insert_races(cursor):
    # Query to insert data into the races table
    query = "INSERT INTO races (races_name, races_faction) VALUES(?, ?)"

    # Loops through each tuple in wow_races, adds data to races table
    for race in constants.WOW_RACES:
        cursor.execute(query, race)
