import unittest
from api.character import Character
from steps import step1

class Step1Tests(unittest.TestCase):
    def setUp(self):
        self.empty_abilities = {
            'Communication': None, 'Constitution': None, 'Cunning': None, 'Dexterity': None,
            'Magic': None, 'Perception': None, 'Strength': None, 'Willpower': None}

    def test_step1_generation_type1(self):
        person = Character()

        self.assertEqual(person.abilities, self.empty_abilities)

        raw_scores = generate_raw_scores()
        self.assertEqual(len(raw_scores), 8)
        for raw_score in raw_scores:
            self.assertTrue(3 <= raw_score <= 18)

        parsed_scores = parse_raw_scores(raw_scores)
        self.assertEqual(len(parsed_scores), 8)
        for parsed_score in parsed_scores:
            self.assertTrue(-2 <= parsed_score <= 4)

        apply_in_order(person, parsed_scores)

        self.assertEqual(person.abilities.values(), parsed_scores)


