import unittest
from api.character import Character
from steps import step1

class Step1Tests(unittest.TestCase):
    def setUp(self):
        self.person = Character()
        self.empty_abilities = {
            'Communication': None, 'Constitution': None, 'Cunning': None, 'Dexterity': None,
            'Magic': None, 'Perception': None, 'Strength': None, 'Willpower': None}

        self.assertEqual(self.person.abilities, self.empty_abilities)

    def test_step1_generation_type1(self):
        raw_scores = step1.generate_raw_scores()
        self.assertEqual(len(raw_scores), 8)
        for raw_score in raw_scores:
            self.assertTrue(3 <= raw_score <= 18)

        parsed_scores = step1.parse_raw_scores(raw_scores)
        self.assertEqual(len(parsed_scores), 8)
        for parsed_score in parsed_scores:
            self.assertTrue(-2 <= parsed_score <= 4)

        step1.apply_in_order(self.person, parsed_scores)

        self.assertEqual(list(self.person.abilities.values()), parsed_scores)

    def test_step1_generation_type2(self):
        """ Note: Requires user input right now. """
        raw_scores = step1.generate_raw_scores()
        self.assertEqual(len(raw_scores), 8)
        for raw_score in raw_scores:
            self.assertTrue(3 <= raw_score <= 18)

        parsed_scores = step1.parse_raw_scores(raw_scores)
        self.assertEqual(len(parsed_scores), 8)
        for parsed_score in parsed_scores:
            self.assertTrue(-2 <= parsed_score <= 4)

        step1.apply_in_any_order(self.person, parsed_scores)

        for ability_score in self.person.abilities.values():
            self.assertTrue(ability_score is not None)

        self.assertEqual(sorted(self.person.abilities.values()),
                         sorted(step1.parse_raw_scores(raw_scores)))

    def test_step1_generation_type3(self):
        """ Note: Requires user input right now. """
        step1.buy_abilities(self.person)

        self.assertEqual(sum(self.person.abilities.values()), 10)

        for ability_score in self.person.abilities.values():
            self.assertTrue(ability_score is not None)
            self.assertTrue(0 <= ability_score <= 3)
