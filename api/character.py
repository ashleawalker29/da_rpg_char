""" This module contains the Character class to which all attributes will be assigned. """
from api.constants import TAB


class Character(object):
    def __init__(self):
        self.abilities = {'Communication': None, 'Constitution': None, 'Cunning': None,
                          'Dexterity': None, 'Magic': None, 'Perception': None, 'Strength': None,
                          'Willpower': None}

    def output_abilities(self):
        for ability, score in self.abilities.items():
            if score is not None:
                print('%s%s: %s' % (TAB, ability, score))
                continue
            print('%s%s: ' % (TAB, ability))
