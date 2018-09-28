from faker import Faker
from random import randint
import calendar
fake = Faker('en_GB')


def example(survey):

    def question_response(question):
        if question['type'] == 'boolean':
            val = fake.boolean() if fake.boolean() else None
            return val
        if question['type'] == 'shortText':
            val = fake.sentence(nb_words=10, variable_nb_words=True) if fake.boolean() else None
            return val
        if question['type'] == 'paragraph':
            val = fake.paragraph(nb_sentences=3, variable_nb_sentences=True) if fake.boolean() else None
            return val
        if question['type'] == 'integer':
            val = randint(question.get('min', 0), question.get('max', 100)) if fake.boolean() else None
            return val
        if question['type'] == 'time':
            val = randint(question.get('min', 0), question.get('max', 100)) if fake.boolean() else None
            return val
        if question['type'] == 'date':
            val = calendar.timegm(fake.date_between(start_date="-3y", end_date="today").timetuple()) if fake.boolean() else None
            return val
        if question['type'] == 'singleChoice':
            val = randint(1, len(question.get('choices').keys())) if fake.boolean() else None
            return val
        if question['type'] == 'multipleChoice':
            val = [randint(1, len(question.get('choices').keys())) for i in range(randint(1, len(question.get('choices').keys())))] if fake.boolean() else None
            return val
        if question['type'] == 'leftHandScale' or question['type'] == 'rightHandScale' or question['type'] == 'centeredScale':
            val = randint(1, question.get('range', 7)) if fake.boolean() else None
            return val

    responses = list(filter(
        lambda r: r['response'] is not None,
        [{'name': q['name'], 'response': question_response(q)} for q in survey['questions']]
    ))

    return {
        'survey': survey['_id'],
        'questions': responses
    }
