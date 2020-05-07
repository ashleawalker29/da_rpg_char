import os

# Constants for printing things to the console nicely.
TAB = '    '
BULLET_POINT = '\u2022'

# Constants for ability names
COM = 'Communication'
CON = 'Constitution'
CUN = 'Cunning'
DEX = 'Dexterity'
MAG = 'Magic'
PER = 'Perception'
STR = 'Strength'
WIL = 'Willpower'

def clear_screen():
    """ Clears the screen. """
    os.system('cls' if os.name == 'nt' else 'clear')
