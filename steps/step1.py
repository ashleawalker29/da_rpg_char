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
    elif generation_type == 2:
        apply_in_any_order(person, parse_raw_scores(generate_raw_scores()))
    elif generation_type == 3:
        buy_abilities(person)


def apply_in_order(person, scores):
    abilities = [COM, CON, CUN, DEX, MAG, PER, STR, WIL]
    person.abilities = dict(zip(abilities, scores))


def apply_in_any_order(person, scores):

    def apply_score(person, ability, score):
        person.abilities[ability] = scores[0]
        del scores[0]

    def meets_requirements(person, choice, ability):
        return (choice in (ability.lower(), ability[:3]) and person.abilities[ability] is None)

    while scores:
        clear_screen()
        print('Your unallocated scores are: %s\n'
              'Your Ability Scores are:' % scores)

        person.output_abilities()

        choice = (input(
            '\nChoose which ability you would like to assign %d to.\n' %
            scores[0]).strip()).lower()

        if meets_requirements(person, choice, COM):
            apply_score(person, COM, scores)
        elif meets_requirements(person, choice, CON):
            apply_score(person, CON, scores)
        elif meets_requirements(person, choice, CUN):
            apply_score(person, CUN, scores)
        elif meets_requirements(person, choice, DEX):
            apply_score(person, DEX, scores)
        elif meets_requirements(person, choice, MAG):
            apply_score(person, MAG, scores)
        elif meets_requirements(person, choice, PER):
            apply_score(person, PER, scores)
        elif meets_requirements(person, choice, STR):
            apply_score(person, STR, scores)
        elif meets_requirements(person, choice, WIL):
            apply_score(person, WIL, scores)


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
    return scores


def buy_abilities(person):

    def increment_score(person, ability, advancement_points):
        person.abilities[ability] += 1
        return advancement_points - 1

    def meets_requirements(person, choice, ability):
        return (choice in (ability.lower(), ability[:3]) and person.abilities[ability] < 3)

    advancement_points = 10

    abilities = [COM, CON, CUN, DEX, MAG, PER, STR, WIL]
    initial_scores = [0, 0, 0, 0, 0, 0, 0, 0]
    person.abilities = dict(zip(abilities, initial_scores))

    while advancement_points:
        clear_screen()
        print('Your Ability Scores are:')

        person.output_abilities()

        print('\nYou have [%s] points to spend.' % advancement_points)
        choice = (input('\nChoose which ability you would like to increment: '))

        if meets_requirements(person, choice, COM):
            advancement_points = increment_score(person, COM, advancement_points)
        elif meets_requirements(person, choice, CON):
            advancement_points = increment_score(person, CON, advancement_points)
        elif meets_requirements(person, choice, CUN):
            advancement_points = increment_score(person, CUN, advancement_points)
        elif meets_requirements(person, choice, DEX):
            advancement_points = increment_score(person, DEX, advancement_points)
        elif meets_requirements(person, choice, MAG):
            advancement_points = increment_score(person, MAG, advancement_points)
        elif meets_requirements(person, choice, PER):
            advancement_points = increment_score(person, PER, advancement_points)
        elif meets_requirements(person, choice, STR):
            advancement_points = increment_score(person, STR, advancement_points)
        elif meets_requirements(person, choice, WIL):
            advancement_points = increment_score(person, WIL, advancement_points)
