from src.database import database
from src import constants

if __name__ == '__main__':
    database.database_setup(constants.DB_NAME)
