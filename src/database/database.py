"""
This file is called at the start of the main function to create all tables
required. The database is being used as a safe way to store player data, loot tables
etc. Current Tables include:
    - Characters
    - Currency
    - Races
    - Classes
    - Specializations
"""

import sqlite3

from src.database.models.characters_model import characters_model
from src.database.models.currency_model import currency_model
from src.database.models.races_model import races_model

from src.database.models.classes_model import classes_model


def database_setup(database_name):
    # Define the connection and cursor
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    # Create tables
    characters_model.create_table(cursor)
    currency_model.create_table(cursor)
    races_model.create_table(cursor)
    classes_model.create_table(cursor)

    # Insert initial data
    races_model.insert_races(cursor)
    classes_model.insert_classes(cursor)

    # Add changes to the database
    connection.commit()

    # Close the connection
    connection.close()

