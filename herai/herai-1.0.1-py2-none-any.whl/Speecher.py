import speech_recognition as sr
from os import system
import random
import sqlite3


class Speecher(object):

    def __init__(self, dbpath):
        self.connection = sqlite3.connect(dbpath)
        self.r = sr.Recognizer()
        self.lastmessage = None
        self.st = False

    def say(self, msg, audio=False):
        if audio:
            system('say ' + msg)

        return msg

    def listen(self, user_text=None):
        out = ''

        if not self.lastmessage:
            self.say('hello')
            self.lastmessage = 'hello'

        if not user_text:
            with sr.Microphone() as source:
                    audio = self.r.listen(source)

            user_text = self.r.recognize_google(audio)

        try:
            my_text = self.answer(user_text.replace("'", ''))

            self.st = False
            out = self.say(my_text)

            self.learn(
                self.lastmessage.replace("'", ''), user_text.replace("'", ''))

            self.lastmessage = my_text
            self.st = True
        except (LookupError, sr.UnknownValueError):
                print('Woops, error.... I have to think a little bit...')
                return

        return out

    def learn(self, input, output):
        c = self.connection.cursor()
        c.execute(
            'INSERT INTO messages (input, output)' +
            'VALUES("'+input+'", "'+output+'")'
        )
        self.connection.commit()
        c.close()

    def answer(self, input):
        c = self.connection.cursor()

        c.execute("SELECT output FROM messages WHERE input LIKE '%"+input+"%'")
        answers = c.fetchall()

        if len(answers) > 0:
            return answers[random.randrange(0, len(answers))][0]

        perfect_answers = []
        bad_answers = []

        c.execute("SELECT output FROM messages")
        answers = c.fetchall()
        c.close()

        if len(answers) == 0:
            return 'sorry?'
        else:
            for ans in answers:
                if ans[0].find(input) > 0 or ans[0] == input:
                    perfect_answers.append(ans[0])

            if len(perfect_answers) == 0:
                for ans in answers:
                    for word in input.split(' '):
                        if ans[0].find(word) > 0 and\
                                random.randrange(0, 3) == 0:
                            bad_answers.append(ans[0])

        if len(perfect_answers) > 0:
            return perfect_answers[random.randrange(0, len(perfect_answers))]

        else:
                if len(bad_answers) > 0:
                    return bad_answers[random.randrange(0, len(bad_answers))]
                else:
                    return 'what?'
