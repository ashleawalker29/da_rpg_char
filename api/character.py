""" This module contains the Character class to which all attributes will be assigned. """

class Character(object):
    def __init__(self):
        self.abilities = {'Communication': None, 'Constitution': None, 'Cunning': None,
                          'Dexterity': None, 'Magic': None, 'Perception': None, 'Strength': None,
                          'Willpower': None}
