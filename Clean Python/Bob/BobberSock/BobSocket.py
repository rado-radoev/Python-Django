import string
import re

class Bob():

    ANSWERS = dict()

    def __init__(self):
        self.ANSWERS["question"] = "Sure."
        self.ANSWERS["yell"]= "Whoa, chill out!"
        self.ANSWERS["yell question"] = "Calm down, I know what I'm doing!"
        self.ANSWERS["empty"] = "Fine. Be that way!"
        self.ANSWERS["other"] = "Whatever."

    def hey(self, message):
        return self.check_message_meaning(message)

    def check_message_meaning(self, message):
        bobs_answer = self.ANSWERS.get("other")

        bobs_updated_answer = message.strip()

        if self.is_message_upper(bobs_updated_answer) and self.is_last_char_question_mark(bobs_updated_answer):
            bobs_answer = self.ANSWERS.get("yell question")
        elif self.is_message_upper(bobs_updated_answer):
            bobs_answer = self.ANSWERS.get("yell")
        elif self.is_last_char_question_mark(bobs_updated_answer):
            bobs_answer = self.ANSWERS.get("question")
        elif self.is_message_empyt(bobs_updated_answer):
            bobs_answer = self.ANSWERS.get("empty")

        return bobs_answer

    def is_message_upper(self, message):

        has_at_least_one_char = False
        is_all_upper_case = True

        for c in message:
            if not c.isalpha(): continue
            if c in string.ascii_letters: has_at_least_one_char = True
            if c.islower():
                is_all_upper_case = False
                break


        return has_at_least_one_char and is_all_upper_case

    def is_last_char_question_mark(self, message):
        return len(message) > 0 and message[-1] == '?'

    def is_message_empyt(self, message):
        m = re.search(r'\s[^\w\\?]', message)
        if message == '' or m:
            return True
        else:
            return False