#!/usr/bin/env python3

from steps import step1
from api.character import Character

def main():
    c = Character()

    generation_type = step1.get_ability_score_generation_type()
    print('Got here!')
    step1.ability_score_generation(generation_type, c)

if __name__ == '__main__':
    main()
