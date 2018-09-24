from datetime import datetime
from hashlib import sha1

from release_name_generator.common.utils import generate_name_from_sha1
from release_name_generator.config import adjectives, nouns


class NameGenerator:
    def __init__(self, config=None):
        self.config = {}
        if config is not None:
            self.config = config
        else:
            self.config['nouns'] = nouns
            self.config['adjectives'] = adjectives

        self.nouns = self.config['nouns']
        self.adjectives = self.config['adjectives']

    def generate_name_by_ref(self, ref_name):
        name = generate_name_from_sha1(self.nouns, self.adjectives, ref_name)
        return name

    def generate_name_by_date(self, date_from, date_to):
        date_from = datetime.strptime(date_from, '%d-%m-%Y')
        date_to = datetime.strptime(date_to, '%d-%m-%Y')

        date_hash = sha1(f'{date_from} - {date_to}'.encode('utf-8')).hexdigest()

        name = generate_name_from_sha1(self.nouns, self.adjectives, date_hash)
        return name
