# Database
DB_NAME = 'world_of_warcraft.db'

# Dictionary of classes with respective races (primary keys of races)
CLASS_RACE_IDS = {"Warrior": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                  "Paladin": [1, 2, 5, 9, 10, 15, 17, 23],
                  "Hunter": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                  "Rogue": [1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24],
                  "Priest": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24],
                  "Shaman": [2, 5, 7, 10, 11, 13, 15, 16, 18, 19, 21, 22, 23, 24],
                  "Mage:": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 23, 24],
                  "Warlock": [1, 2, 4, 6, 8, 10, 12, 13, 14, 16, 17, 18, 20, 24],
                  "Monk": [1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24],
                  "Druid": [3, 6, 11, 15, 16, 21, 23],
                  "Demon Hunter": [3, 17],
                  "Death Knight": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
                  }

# List of tuples containing all races and their faction
WOW_RACES = [('Human', 'Alliance'),
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
             ('Vulpera', 'Horde')]
