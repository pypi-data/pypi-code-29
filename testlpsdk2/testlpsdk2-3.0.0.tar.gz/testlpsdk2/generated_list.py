import json
import logging
import os
import sys
import requests

from lyrebird import Lyrebird

if len(sys.argv) != 2:
    print('usage: python ' + sys.argv[0] + ' <lyrebird-token>')
    exit(1)
access_token = sys.argv[1]


logging.basicConfig()
logger = logging.getLogger('logger')

client = Lyrebird(access_token=access_token, logger=logger)
client.logger.setLevel(logging.DEBUG)

first_utterance = 'Hello World'
second_utterance = 'My vocal avatar is very cool!'

# Generate two utterances
client.generate(first_utterance)
client.generate(second_utterance)

# Get the last two generated utterances
generated_resp = client.generated(0, 2)
generated_resp_json = generated_resp.json()

# Get the count of all the utterances generated
count = generated_resp_json['count']

# Get the first utterance text and synthethised audio
utterances = generated_resp_json['results']
first_utterance_text = utterances[0]['text']
first_utterance_url = utterances[0]['url']

print('The audio of the utterance "{0}" is located at {1}'.format(
    first_utterance_text, first_utterance_url))
