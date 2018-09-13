import json
import logging
import os
import sys
import requests

from playsound import playsound
from lyrebirdaii import Lyrebird

logging.basicConfig()
logger = logging.getLogger('logger')

if len(sys.argv) != 3:
    print(
        'usage: python ' +
        sys.argv[0] +
        ' <lyrebird-token>' +
        ' <utterance>')
    exit(1)

access_token = sys.argv[1]
utterance = sys.argv[2]

client = Lyrebird(access_token=access_token, logger=logger)
client.logger.setLevel(logging.DEBUG)

response = client.generate(utterance)
with open('hello_world.wav', "wb+") as audio_file:
    audio_file.write(response.content)
playsound('hello_world.wav')
