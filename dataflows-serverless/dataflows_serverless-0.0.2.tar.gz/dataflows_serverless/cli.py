from os import path
import dataflows_serverless
from dataflows_serverless.constants import DEFAULT_IMAGE


def bin():
    print(path.join(path.dirname(dataflows_serverless.__file__), 'bin'))


def image():
    print(DEFAULT_IMAGE)
