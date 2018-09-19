from __future__ import print_function
from __future__ import unicode_literals
# coding : utf-8
from hermes_python.hermes import Hermes

def callback_encoding_test(hermes, intentMessage):
    print(intentMessage)

with Hermes("raspi3-14.local") as h:
    h.subscribe_intent("lightsSet", callback_encoding_test).loop_forever()


