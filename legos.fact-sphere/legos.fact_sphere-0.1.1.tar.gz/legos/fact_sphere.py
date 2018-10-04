from Legobot.Lego import Lego
import logging
import os
import random
import yaml

logger = logging.getLogger(__name__)


class FactSphere(Lego):
    def listening_for(self, message):
        if message.get('text'):
            try:
                if message.get('text').startswith('!fact'):
                    return True
            except Exception as e:
                logger.error(('FactSphere lego failed to check the message'
                             ' text: {}'.format(e)))
                return False

    def handle(self, message):
        opts = self.set_opts(message)
        fact = self._get_random_fact()
        if fact is not None:
            response = self._format_response(fact)
            self.reply(message, response, opts)
        else:
            logger.error('There was an issue handling the message.')

    def _get_random_fact(self):
        facts = self._load_fact_data()
        if facts is not None:
            fact = random.choice(facts['facts'])  # nosec
            return fact
        else:
            return None

    def _format_response(self, fact):
        response = '> {}\n-The Fact Sphere\n({})'.format(fact['fact'],
                                                         fact['audio'])
        return response

    def _load_fact_data(self):
        path = os.path.dirname(__file__)
        fact_file = path + '/facts.yaml'
        try:
            with open(fact_file, 'r') as f:
                facts = yaml.safe_load(f)
            return facts
        except Exception as e:
            logger.error('Error loading facts file: {}'.format(e))
            return None

    def set_opts(self, message):
        try:
            target = message['metadata']['source_channel']
            opts = {'target': target}
            return opts
        except Exception as e:
            logger.error(('Could not identify message source in '
                         'message. Error: {}'.format(e)))

    def get_name(self):
        return 'fact_sphere'

    def get_help(self):
        return '!fact to return a random Fact Sphere fact.'
