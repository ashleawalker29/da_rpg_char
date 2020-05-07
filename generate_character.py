#!/usr/bin/env python3

from api.character import Character
from steps import step1

def main():
    c = Character()

    generation_type = step1.get_ability_score_generation_type()
    step1.ability_score_generation(generation_type, c)

if __name__ == '__main__':
    main()
