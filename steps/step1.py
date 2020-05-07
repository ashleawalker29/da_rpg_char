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

    while scores:
        clear_screen()
        print('Your unallocated scores are: %s\n'
              'Your Ability Scores are:' % scores)

        person.output_abilities()

        # make the input lowercase just to make comparison easier
        ability = (input(
            '\nChoose which ability you would like to assign %d to.\n' %
            scores[0]).strip()).lower()

        # Check input against possible abilities. Make sure we don't override any abilities that
        # have just been set.
        if (ability in (COM.lower(), 'com', '1') and
                person.abilities[COM] is None):
            apply_score(person, COM, scores)
        elif (ability in (CON.lower(), 'con', '2') and
              person.abilities[CON] is None):
            apply_score(person, CON, scores)
        elif (ability in (CUN.lower(), 'cun', '3') and
              person.abilities[CUN] is None):
            apply_score(person, CUN, scores)
        elif (ability in (DEX.lower(), 'dex', '4') and
              person.abilities[DEX] is None):
            apply_score(person, DEX, scores)
        elif (ability in (MAG.lower(), 'mag', '5') and
              person.abilities[MAG] is None):
            apply_score(person, MAG, scores)
        elif (ability in (PER.lower(), 'per', '6') and
              person.abilities[PER] is None):
            apply_score(person, PER, scores)
        elif (ability in (STR.lower(), 'str', '7') and
              person.abilities[STR] is None):
            apply_score(person, STR, scores)
        elif (ability in (WIL.lower(), 'wil', 'will', '8') and
              person.abilities[WIL] is None):
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
    print(scores)
    return scores


def buy_abilities(person):

    def increment_score(person, ability, advancement_points):
        person.abilities[ability] += 1
        return advancement_points - 1

    advancement_points = 10

    abilities = [COM, CON, CUN, DEX, MAG, PER, STR, WIL]
    initial_scores = [0, 0, 0, 0, 0, 0, 0, 0]
    person.abilities = dict(zip(abilities, initial_scores))

    while advancement_points:
        clear_screen()
        print('Your Ability Scores are:')

        person.output_abilities()

        # make the input lowercase just to make comparison easier
        print('\nYou have [%s] points to spend.' % advancement_points)
        ability = (input('\nChoose which ability you would like to increment: '))

        # Check input against possible abilities. Make sure we don't override any abilities that
        # have just been set.
        if (ability in (COM.lower(), 'com', '1') and person.abilities[COM] < 3):
            advancement_points = increment_score(person, COM, advancement_points)
        elif (ability in (CON.lower(), 'con', '2') and person.abilities[CON] < 3):
            advancement_points = increment_score(person, CON, advancement_points)
        elif (ability in (CUN.lower(), 'cun', '3') and person.abilities[CUN] < 3):
            advancement_points = increment_score(person, CUN, advancement_points)
        elif (ability in (DEX.lower(), 'dex', '4')and person.abilities[DEX] < 3):
            advancement_points = increment_score(person, DEX, advancement_points)
        elif (ability in (MAG.lower(), 'mag', '5')and person.abilities[MAG] < 3):
            advancement_points = increment_score(person, MAG, advancement_points)
        elif (ability in (PER.lower(), 'per', '6')and person.abilities[PER] < 3):
            advancement_points = increment_score(person, PER, advancement_points)
        elif (ability in (STR.lower(), 'str', '7')and person.abilities[STR] < 3):
            advancement_points = increment_score(person, STR, advancement_points)
        elif (ability in (WIL.lower(), 'wil', 'will', '8')and person.abilities[WIL] < 3):
            advancement_points = increment_score(person, WIL, advancement_points)
