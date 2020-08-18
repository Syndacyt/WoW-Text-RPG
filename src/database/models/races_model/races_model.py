"""
This file is initially ran through database.py function database_setup(). The main purpose of this file is to
create the table for races and populate the table with all the current playable races in World of Warcraft.

All races can be found at:
https://worldofwarcraft.com/en-us/game/races
"""

import sqlite3


def create_table(cursor):
    """
    This function is used to initially create the table. It should not be called again unless the database is being
    reset. Should only be called in database.py database_setup().

    :param cursor: sqlite3 cursor object
    """
    try:
        cursor.execute(""" CREATE TABLE IF NOT EXISTS races (
            races_id INTEGER PRIMARY KEY NOT NULL,
            races_name TEXT NOT NULL,
            races_faction TEXT NOT NULL)
        """)

    except sqlite3.OperationalError as e:
        print('sqlite error: ', e.args[0])


def insert_races(cursor):
    """
    Create a list containing tuples of races that include the race name and faction they are associated with. This list
    if then used to insert data into the races table.

    :param cursor: sqlite3 cursor object
    """

    # Query to insert data into the races table
    query = "INSERT INTO races (races_name, races_faction) VALUES(?, ?)"

    # List of playable races and their factions
    wow_races = [
        # Alliance
        ('Human', 'Alliance'),
        ('Dwarf', 'Alliance'),
        ('Night Elf', 'Alliance'),
        ('Gnome', 'Alliance'),
        ('Draenei', 'Alliance'),
        ('Worgen', 'Alliance'),
        ('Pandaren', 'Alliance'),
        ('Void Elf', 'Alliance'),
        ('Lightforged Draenei', 'Alliance'),
        ('Dark Iron Dwarf', 'Alliance'),
        ('Kul Tiran', 'Alliance'),
        ('Mechagnome', 'Alliance'),

        # Horde
        ('Orc', 'Horde'),
        ('Undead', 'Horde'),
        ('Tauren', 'Horde'),
        ('Troll', 'Horde'),
        ('Blood Elf', 'Horde'),
        ('Goblin', 'Horde'),
        ('Pandaren', 'Horde'),
        ('Nightborne', 'Horde'),
        ('Highmountain Tauren', 'Horde'),
        ("Mag'har Orc", 'Horde'),
        ('Zandalari Troll', 'Horde'),
        ('Vulpera', 'Horde')
    ]

    # Loops through each tuple in wow_races, adds data to races table
    for race in wow_races:
        cursor.execute(query, race)
