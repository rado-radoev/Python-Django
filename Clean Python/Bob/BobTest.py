import unittest

from Bob import Bob

class BobTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bob = Bob()


    def test_say_something(self):
        self.assertEqual("Whatever.", self.bob.hey("Tom-ay-to, tom-aaaah-to."))

    def test_shouting(self):
        self.assertEqual("Whoa, chill out!", self.bob.hey("WATCH OUT!"))

    def test_shouting_gibberish(self):
        self.assertEqual("Whoa, chill out!", self.bob.hey('FCECDFCAAB'))

    def test_asking_question(self):
        self.assertEquals("Sure.", self.bob.hey("Does this cryogenic chamber make me look fat?"))

    def test_asking_numeric_question(self):
        self.assertEquals("Sure.",self.bob.hey("You are, what, like 15?"))

    def test_asking_gibberish(self):
        self.assertEqual("Sure.", self.bob.hey("fffbbcbeab?"))

    def test_talking_forcefully(self):
        self.assertEqual("Whatever.", self.bob.hey("Let's go make out behind the gym!"))

    def test_using_acronyms_in_regular_speech(self):
        self.assertEqual("Whatever.", self.bob.hey("It's OK if you don't want to go to the DMV."))

    def test_foceful_questions(self):
        self.assertEqual("Calm down, I know what I'm doing!", self.bob.hey("WHAT THE HELL WERE YOU THINKING?"))

    def test_shouting_numbers(self):
        self.assertEqual("Whoa, chill out!", self.bob.hey("1, 2, 3 GO!"))

    def test_only_numbers(self):
        self.assertEqual("Whatever.", self.bob.hey("1, 2, 3"))

    def test_question_with_only_numbers(self):
        self.assertEqual("Sure.", self.bob.hey("4?"))

    def test_shouting_with_special_characters(self):
        self.assertEqual("Whoa, chill out!", self.bob.hey("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"))

    def test_shouting_with_no_exclamation_mark(self):
        self.assertEqual("Whoa, chill out!", self.bob.hey("I HATE THE DMV"))

    def test_statement_containing_question_mark(self):
        self.assertEqual("Whatever.", self.bob.hey("Ending with ? means a question."))

    def test_no_letters_with_question_mark(self):
        self.assertEqual("Sure.", self.bob.hey(":) ?"))

    def test_pratt_ling_on(self):
        self.assertEqual("Sure.", self.bob.hey("Wait! Hang on. Are you going to be OK?"))

    def test_silence(self):
        self.assertEqual("Fine. Be that way!", self.bob.hey(""))

    def test_prolonged_silence(self):
        self.assertEqual("Fine. Be that way!", self.bob.hey("         "))

    def test_alternative_silence(self):
        self.assertEquals("Fine. Be that way!", self.bob.hey("{:>10}".format(' ')))

    def test_multiple_line_question(self):
        self.assertEqual("Whatever.", self.bob.hey("\nDoes this cryogenic chamber make me look fat?\nNo."))

    def test_starting_with_whitespace(self):
        self.assertEqual("Whatever.", self.bob.hey("         hmmmmmmm..."))

    def test_ending_with_white_space(self):
        self.assertEquals("Sure.",self.bob.hey("Okay if like my  spacebar  quite a bit?   "))

    def test_other_white_space(self):
        self.assertEqual("Fine. Be that way!", self.bob.hey("\n\r \t"))

if __name__ == '__main__':
    unittest.main()