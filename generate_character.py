#!/usr/bin/env python3
import logging

from api.character import Character
from api.constants import clear_screen
from steps import step1


def main():
    # Initialize the character
    c = Character()

    # Initialize logging
    logging.basicConfig(format='%(message)s', filename='character.log', level=logging.DEBUG)
    logging.info('-*-*-*- BEGIN LOGGING CHARACTER CREATION -*-*-*-')

    logging.info('Step 1: Determine abilities...\n')
    generation_type = step1.get_ability_score_generation_type()
    step1.ability_score_generation(generation_type, c)
    clear_screen()
    c.output_abilities()
    logging.info('\nStep 1: COMPLETE')


if __name__ == '__main__':
    main()
