from api.dice_roll import roll
from api.constants import TAB, COM, CON, CUN, DEX, MAG, PER, STR, WIL, clear_screen

def get_ability_score_generation_type():
    while True:
        choice = int(input('There are three options of generating your ability scores.\n'
                           '%s1. Assigned in the order the scores are generated.\n'
                           '%s2. Arranged in an order or your choice.\n'
                           '%s3. Buying abilities.\n\n'
                           'Please enter the number of the generation type you would like: '
                           % (TAB, TAB, TAB)))
        if choice in [1, 2, 3]:
            return choice

def ability_score_generation(generation_type, person):
    if generation_type == 1:
        apply_in_order(person, parse_raw_scores(generate_raw_scores()))

def apply_in_order(person, scores):
    abilities = [COM, CON, CUN, DEX, MAG, PER, STR, WIL]
    person.abilities = dict(zip(abilities, scores))

def generate_raw_scores():
    scores = [roll(1, 6) + roll(1, 6) + roll(1, 6) for _ in range(8)]
    return scores

def parse_raw_scores(raw_scores):
    scores = []
    for score in raw_scores:
        if score == 3:
            scores.append(-2)
        elif score in (4, 5):
            scores.append(-1)
        elif score in (6, 7, 8):
            scores.append(0)
        elif score in (9, 10, 11):
            scores.append(1)
        elif score in (12, 13, 14):
            scores.append(2)
        elif score in (15, 16, 17):
            scores.append(3)
        elif score == 18:
            scores.append(4)
    print(scores)
    return scores
